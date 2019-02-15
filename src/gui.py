import json
import tkinter as tk


'''
    Renders the title
'''
def render_title(date):

    # Panel
    pane = tk.PanedWindow()
    pane.pack(fill = tk.X, expand = 1, side = tk.TOP, pady = (20, 20))

    font = 'Inherit 20 bold'

    tk.Label(pane, text = date, font = font).pack()


'''
    Renders the puzzle grid
'''
def render_grid(puzzle):

    # Panel
    pane = tk.PanedWindow()
    pane.pack(fill = tk.X, expand = 1, side = tk.LEFT, padx = (10, 10), pady = (20, 20))

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

            # Label dimensions
            height = 10 - dimension
            width = height * 2

            tk.Label(pane, text = number + letter, font = font, bg = bg, width = width, height = height, relief = tk.RIDGE).grid(row = i, column = j)

'''
    Renders the clues
'''
def render_clues(clues):

    # Fonts
    font = 'Inherit 14 normal'
    font_b = 'Inherit 14 bold'

    # Wrapper panel
    pane = tk.PanedWindow()
    pane.pack(fill = tk.X, side = tk.RIGHT)

    # Across Pane & its title
    across_pane = tk.PanedWindow()
    across_pane.pack(fill = tk.X, side = tk.TOP, padx = (20, 20), pady = (20, 20))
    tk.Label(across_pane, text = 'ACROSS', font = font_b).pack()

    # Down Pane & its title
    down_pane = tk.PanedWindow()
    down_pane.pack(fill = tk.X, padx = (20, 20), pady = (20, 20))
    tk.Label(down_pane, text = 'DOWN', font = font_b).pack()

    for clue in clues['across']:
        clue = clue['number'] + '. ' +  clue['clue']
        tk.Label(across_pane, text = clue, font = font, wraplength = 300).pack()

    for clue in clues['down']:
        clue = clue['number'] + '. ' +  clue['clue']
        tk.Label(down_pane, text = clue, font = font, wraplength = 300).pack()


'''
    Renders all elements
'''
def render(data):

    # ROOT
    root = tk.Tk()
    root.title('NY Times Crossword')

    if data is None or data['date'] is None or data['puzzle'] is None or data['clues'] is None:
        print("ERROR: Data is not in proper format!")
        return

    render_title(data['date'])
    render_grid(data['puzzle'])
    render_clues(data['clues'])

    root.resizable(False, False)
    root.mainloop()
