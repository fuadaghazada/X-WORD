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

        self.__root = None

    '''
        Renders the title
    '''
    def __render_title(self, date):

        # Panel
        pane = tk.PanedWindow()
        pane.pack(fill = tk.X, expand = 1, side = tk.TOP, pady = (20, 20))

        font1 = 'Inherit 20 bold'
        font2 = 'Inherit 16 italic'

        tk.Label(pane, text = "X-WORD NYTime Crossword Clue Generator", font=font1).pack()
        tk.Label(pane, text = date, font = font2).pack()

        # LOG
        self.log_gen.write_to_file('Title is rendered')
        print('\tTitle is rendered')


    '''
        Renders the puzzle grid
    '''
    def __render_grid(self, puzzle):

        # Panel
        canvas = tk.Canvas(self.__root, width = 505, height = 505)
        canvas.pack(fill = tk.BOTH, side = tk.LEFT)

        # Gap from left edge of screen
        GAP = 5
        tmp = (int(canvas['width']) - GAP * 2)

        # Dimension of the puzzle
        dimension = len(puzzle)

        letter_font = ('Arial', str(tmp // 11))
        number_font = ('Arial', str(tmp // 20))

        # Width of the cell
        w = tmp / dimension

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
                        number = str(puzzle[i][j][0])

                # Grid components
                canvas.create_rectangle(j * w + GAP, i * w + GAP, j * w + w + GAP, i * w + w + GAP, fill = bg, outline = 'gray', width = 1.5)
                canvas.create_text(j * w + w / 2 + GAP, i * w + w / 3 + GAP, text = letter, width = 100, font = letter_font, fill = "#2860d8")
                canvas.create_text(j * w + 15 + GAP, i * w + 25 + GAP, text = number, width = 100, font = number_font)

        # LOG
        self.log_gen.write_to_file('Grids are rendered')
        print('\tGrids are rendered')


    '''
        Renders the clues
    '''
    def __render_clues(self, clues, title):

        # Fonts
        font = 'Inherit 14 normal'
        font_b = 'Inherit 14 bold'

        # Wrapper panel
        pane = tk.PanedWindow()
        pane.pack(fill = tk.X, side = tk.TOP)

        # Title
        tk.Label(pane, text = title).pack(fill = tk.BOTH)

        # Across Pane & its title
        across_pane = tk.PanedWindow(pane)
        across_pane.pack(fill = tk.X, side = tk.LEFT, padx = (20, 20), pady = (20, 20))
        tk.Label(across_pane, text = 'ACROSS', font = font_b, anchor='w').pack(fill = tk.BOTH)

        clues_str = ""
        for clue in clues['across']:
            clues_str += clue['number'] + '. ' + clue['clue'] + "\n\n"
        tk.Label(across_pane, text = clues_str, font = font, wraplength = 450, justify=tk.LEFT).pack(fill = tk.BOTH)

        # Down Pane & its title
        down_pane = tk.PanedWindow(pane)
        down_pane.pack(fill = tk.X, side = tk.RIGHT, padx = (20, 20), pady = (20, 20))
        tk.Label(down_pane, text = 'DOWN', font = font_b, anchor='w').pack(fill = tk.BOTH)

        clues_str = ""
        for clue in clues['down']:
            clues_str += clue['number'] + '. ' + clue['clue'] + "\n\n"
        tk.Label(down_pane, text = clues_str, font = font, wraplength = 450, justify=tk.LEFT).pack(fill = tk.BOTH)

        # LOG
        self.log_gen.write_to_file('Clues are rendered')
        print('\tClues are rendered')


    '''
        Renders all elements
    '''
    def render(self, data):

        # ROOT
        self.__root = tk.Tk()
        self.__root.title('NY Times Crossword')
        # self.__root.geometry('1000x1000')

        # LOG
        print("---Showing the puzzle----\n")
        self.log_gen.write_to_file('Window is constructed')
        print('\tWindow is constructed')

        if data is None or data['date'] is None or data['puzzle'] is None or data['clues'] is None:
            print("ERROR: Data is not in proper format!")
            return

        self.__render_title(data['date'])
        self.__render_grid(data['puzzle'])
        self.__render_clues(data['clues'], 'Original Clues')
        self.__render_clues(data['generated_clues'], 'Generated Clues')

        print("---------------------------")

        self.__root.resizable(False, False)
        self.__root.mainloop()
