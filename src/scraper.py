import os
import sys
import math
import time
import json

import bs4
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

'''
    Puzzle Scraper
'''
class PuzzleScraper:

    # NYTimes Crossword URL
    URL = 'https://www.nytimes.com/crosswords/game/mini'

    '''
        Constructor
    '''
    def __init__(self, log_gen):
        # Log generator obj
        self.log_gen = log_gen

    '''
        Fetching the puzzle
    '''
    def fetch_puzzle(self):
        # Sending request to the URL
        req = self.__reveal_answer()

        if req is None:
            return None

        # Scraper
        soup = bs4.BeautifulSoup(req, 'html.parser')

        date = soup.find('div', attrs={'class' : 'PuzzleDetails-date--1HNzj'}).text
        puzzle = soup.find('g', attrs={'data-group' : 'cells'})
        clues = soup.find('section', attrs={'class' : 'Layout-clueLists--10_Xl'})

        # Getting clues and solution
        clues = self.__fetch_clues(clues)
        puzzle = self.__fetch_cells(puzzle)

        # Data for return
        data = {
            'date' : date,
            'puzzle' : puzzle,
            'clues' : clues
        }

        # Writing data in JSON format to the file with date name in 'data' folder or project dir
        filename = os.getcwd() + '/data/' + str(date).replace(" ", "") + '.json'

        if '/src' in filename:
            filename = filename.replace("/src", '')

        w_data = json.dumps(data)

        with open(filename, 'w') as outfile:
            outfile.write(w_data)

        # LOG
        self.log_gen.write_to_file('Puzzle data is written to the JSON file')

        return data


    '''
        Opening browser -> Revealing answer -> Returning page source
    '''
    def __reveal_answer(self):

        timeout = 5
        try:
            # Opening browser
            driver = webdriver.Chrome()
            driver.get(self.URL)

            # LOG
            self.log_gen.write_to_file('Browser is opened and request is sent to the URL')

            try:
                # Waiting for modal fully loaded
                modal = EC.presence_of_element_located((By.CLASS_NAME, "ModalBody-body--3PkKz"))
                WebDriverWait(driver, timeout).until(modal)

                # LOG
                self.log_gen.write_to_file('Page is loaded')

                # CLicking to start btn
                start_btn = driver.find_element_by_css_selector(".buttons-modalButton--1REsR")
                start_btn.click()

                # Waiting for toolbar fully loaded
                toolbar = EC.presence_of_element_located((By.CSS_SELECTOR, ".Tool-button--39W4J.Tool-tool--Fiz94.Tool-texty--2w4Br"))
                WebDriverWait(driver, timeout).until(toolbar)

                # 'Reveal'
                reveal_btn = driver.find_element_by_css_selector(".Toolbar-expandedMenu--2s4M4").find_elements_by_css_selector(".Tool-button--39W4J.Tool-tool--Fiz94.Tool-texty--2w4Br")[1]
                reveal_btn.click()

                # 'Puzzle'
                puzzle_btn = reveal_btn.find_elements_by_css_selector(".HelpMenu-item--1xl0_")[2]
                puzzle_btn.click()

                # LOG
                self.log_gen.write_to_file('Reveal Puzzle is clicked!')

            except TimeoutException:
                print("TIMEOUT")
                sys.exit()

            # CONGRATULATIONS!!!
            driver.find_element_by_css_selector('html').send_keys(u'\ue007')
            driver.find_element_by_css_selector('html').send_keys(u'\ue00c')

            # It will be scraped, so will be returned
            p_source = driver.page_source

            # Closing browser
            driver.close()

            # LOG
            self.log_gen.write_to_file('Browser is closed and content of the page is returned')

        except Exception as e:
            p_source = None
            raise

        return p_source


    '''
        Fetching the clues
    '''
    def __fetch_clues(self, clues):
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

        # LOG
        self.log_gen.write_to_file('Across clues are parsed from the page content')

        # Down
        down = divs[1].find('ol').find_all('li')
        down_data = []
        for li in down:
            down_data.append({
                'number' : li.findChildren()[0].text,
                'clue' : li.findChildren()[1].text
            })

        # LOG
        self.log_gen.write_to_file('Down clues are parsed from the page content')

        # Returning whole data
        return {
            'across' : across_data ,
            'down' : down_data
        }


    '''
        Fetching the puzzle cells
    '''
    def __fetch_cells(self, puzzle):
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
            puzzle_data[i][j] = self.__process_cell_data(cell)
            j += 1

        # LOG
        self.log_gen.write_to_file('Puzzle cells are parsed from the page content')

        return puzzle_data


    '''
        Processing the cell data
    '''
    def __process_cell_data(self, cell):

        components = cell.findChildren('text')
        size = len(components)

        '''
            3 Cases:
                components with size 2:
                    cell has both 'number' and 'letter'
                components with size 1:
                    cell has only a 'letter'
                components with size 0:
                    cell is black (empty)
        '''

        if size == 2:
            number = components[0].text
            letter = components[1].text
            return [number, letter]
        elif size == 1:
            letter = components[0].text
            return [letter]
        elif size == 0:
            return None
