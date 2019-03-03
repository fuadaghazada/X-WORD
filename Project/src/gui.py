import tkinter as tk


'''
    GUI for displaying Puzzle
'''

class GUI:

    '''
        Constructor
    '''
    def __init__(self, log_gen):
        # Log generator obj
        self.log_gen = log_gen

    '''
        Renders the title
    '''
    def __render_title(self, date):

        # Panel
        pane = tk.PanedWindow()
        pane.pack(fill = tk.X, expand = 1, side = tk.TOP, pady = (20, 20))

        font = 'Inherit 20 bold'

        tk.Label(pane, text = date, font = font).pack()

        # LOG
        self.log_gen.write_to_file('Title is rendered')


    '''
        Renders the puzzle grid
    '''
    def __render_grid(self, puzzle):

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

        # LOG
        self.log_gen.write_to_file('Grids are rendered')


    '''
        Renders the clues
    '''
    def __render_clues(self, clues):

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

        # LOG
        self.log_gen.write_to_file('Clues are rendered')


    '''
        Renders all elements
    '''
    def render(self, data):

        # ROOT
        root = tk.Tk()
        root.title('NY Times Crossword')

        # LOG
        self.log_gen.write_to_file('Window is constructed')

        if data is None or data['date'] is None or data['puzzle'] is None or data['clues'] is None:
            print("ERROR: Data is not in proper format!")
            return

        self.__render_title(data['date'])
        self.__render_grid(data['puzzle'])
        self.__render_clues(data['clues'])

        root.resizable(False, False)
        root.mainloop()
