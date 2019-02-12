import json

import tkinter as tk
from tkinter import *

from scraper import fetch_puzzle

# Loading data
# with open('data/Tuesday February 12, 2019.json') as f:
#     data = json.load(f)

data = fetch_puzzle()

# ROOT
root = tk.Tk()
root.title('NY Times Crossword')

'''
    Renders the title
'''
def render_title(date):

    # Panel
    pane = PanedWindow()
    pane.pack(fill = X, expand = 1, side = TOP, pady = (20, 20))

    font = 'Inherit 20 bold'

    tk.Label(pane, text = data['date'], font = font).pack()


'''
    Renders the puzzle grid
'''
def render_grid(puzzle):

    # Panel
    pane = PanedWindow()
    pane.pack(fill = X, expand = 1, side = LEFT, padx = (10, 10), pady = (20, 20))

    # Dimension of the puzzle
    dimension = len(puzzle)

    font = 'Inherit 18 bold'

    for i in range(dimension):
        for j in range(dimension):

            number = ''
            letter = ''

            if puzzle[i][j] is None:
                bg = 'black'
            else:
                bg = 'white'
                letter = '\n' + str(puzzle[i][j][len(puzzle[i][j]) - 1])

                if len(puzzle[i][j]) == 2:
                    number = '[' + str(puzzle[i][j][0]) + ']'

            tk.Label(pane, text = number + letter, font = font, bg = bg, width = 5, height = 5, relief = RIDGE).grid(row = i, column = j)


'''
    Renders the clues
'''
def render_clues(clues):

    # Fonts
    font = 'Inherit 14 normal'
    font_b = 'Inherit 14 bold'

    # Wrapper panel
    pane = PanedWindow()
    pane.pack(fill = X, side = RIGHT)

    # Across Pane & its title
    across_pane = PanedWindow()
    across_pane.pack(fill = X, side = TOP, padx = (20, 20), pady = (20, 20))
    tk.Label(across_pane, text = 'ACROSS', font = font_b).pack()

    # Down Pane & its title
    down_pane = PanedWindow()
    down_pane.pack(fill = X, padx = (20, 20), pady = (20, 20))
    tk.Label(down_pane, text = 'DOWN', font = font_b).pack()

    for clue in clues['across']:
        clue = clue['number'] + '. ' +  clue['clue']
        tk.Label(across_pane, text = clue, font = font).pack()

    for clue in clues['down']:
        clue = clue['number'] + '. ' +  clue['clue']
        tk.Label(down_pane, text = clue, font = font).pack()


'''
    Renders all elements
'''
def render(data):

    if data is None:
        return

    render_title(data['date'])
    render_grid(data['puzzle'])
    render_clues(data['clues'])


render(data)

root.resizable(False, False)
root.mainloop()
