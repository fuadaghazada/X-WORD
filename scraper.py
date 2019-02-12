import sys
import math
import time
import json

import bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# NYTimes Crossword URL
URL = 'https://www.nytimes.com/crosswords/game/mini'

'''
    Fetching the puzzle
'''
def fetch_puzzle():
    # Sending request to the URL
    req = reveal_answer()

    if req is None:
        return None

    # Scraper
    soup = bs4.BeautifulSoup(req, 'html.parser')

    date = soup.find('div', attrs={'class' : 'PuzzleDetails-date--1HNzj'}).text
    puzzle = soup.find('g', attrs={'data-group' : 'cells'})
    clues = soup.find('section', attrs={'class' : 'Layout-clueLists--10_Xl'})

    # Getting clues and solution
    clues = fetch_clues(clues)
    puzzle = fetch_cells(puzzle)

    # Data for return
    data = {
        'date' : date,
        'puzzle' : puzzle,
        'clues' : clues
    }

    # Writing data in JSON format to the file with date name in 'data' folder or project dir
    filename = 'data/' + str(date).replace(" ", "") + '.json'
    w_data = json.dumps(data)

    with open(filename, 'w') as outfile:
        outfile.write(w_data)

    return data


'''
    Opening browser -> Revealing answer -> Returning page source
'''
def reveal_answer():

    try:
        # Opening browser
        driver = webdriver.Chrome()
        driver.get(URL)

        # ESC for passing modal
        driver.find_element_by_css_selector('html').send_keys(u'\ue00c')

        # Reveal
        btn1 = driver.find_element_by_css_selector(".Toolbar-expandedMenu--2s4M4").find_elements_by_css_selector(".Tool-button--39W4J.Tool-tool--Fiz94.Tool-texty--2w4Br")[1]

        # Busy Loop :/ -  Waiting for page load
        while btn1 is None:
            driver.find_element_by_css_selector('html').send_keys(u'\ue00c')
            btn1 = driver.find_element_by_css_selector(".Toolbar-expandedMenu--2s4M4").find_elements_by_css_selector(".Tool-button--39W4J.Tool-tool--Fiz94.Tool-texty--2w4Br")[1]

        btn1.click()
        btn1.find_elements_by_css_selector(".HelpMenu-item--1xl0_")[2].click()

        # CONGRATULATIONS!!!
        driver.find_element_by_css_selector('html').send_keys(u'\ue007')
        driver.find_element_by_css_selector('html').send_keys(u'\ue00c')

        # It will be scraped, so will be returned
        p_source = driver.page_source

        # Closing browser
        driver.close()

    except Exception as e:
        p_source = None
        raise

    return p_source


'''
    Fetching the clues
'''
def fetch_clues(clues):
    # None clues: PROBLEM
    if clues is None:
        print("ERROR: No clues are found\n")
        return None

    # Across : [0] & Down : [1]
    divs = clues.findChildren('div', attrs={'class' : 'ClueList-wrapper--3m-kd'})

    if len(divs) != 2:
        return None

    # Across
    across = divs[0].find('ol').find_all('li')
    across_data = []
    for li in across:
        across_data.append({
            'number' : li.findChildren()[0].text,
            'clue' : li.findChildren()[1].text
        })

    # Down
    down = divs[1].find('ol').find_all('li')
    down_data = []
    for li in down:
        down_data.append({
            'number' : li.findChildren()[0].text,
            'clue' : li.findChildren()[1].text
        })

    # Returning whole data
    return {
        'across' : across_data ,
        'down' : down_data
    }


'''
    Fetching the puzzle cells
'''
def fetch_cells(puzzle):
    # None puzzle: PROBLEM
    if puzzle is None:
        print("ERROR: No puzzle is found\n")
        return None

    cells = puzzle.find_all('g')

    # If no cells: smth wrong
    if len(cells) == 0:
        return None

    # 2D array for keeping puzzle geometry
    dimension = int(math.sqrt(len(cells)))        # in our case it is 5
    puzzle_data = [[None for x in range(dimension)] for y in range(dimension)]

    i = 0
    j = 0
    for cell in cells:
        if i == dimension:
            break

        if j == dimension:
            i += 1
            j = 0

        # Putting puzzle data into the 2D array
        puzzle_data[i][j] = process_cell_data(cell)
        j += 1

    return puzzle_data


'''
    Processing the cell data
'''
def process_cell_data(cell):

    components = cell.findChildren()
    size = len(components)

    '''
        3 Cases:
            components with size 4:
                cell has both 'number' and 'letter'
            components with size 3:
                cell has only a 'letter'
            components with size 2 or 1:
                cell is black (empty)
    '''

    if size == 4:
        number = components[1].text
        letter = components[2].text
        return [number, letter]
    elif size == 3:
        letter = components[1].text
        return [letter]
    elif size == 2 or size == 1:
        return None


# ---------------TESTING--------------
# data = fetch_puzzle()
