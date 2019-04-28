import re
import os
import sys
import datetime
import tkinter as tk
from tkinter import ttk

'''
    Getting files from 'data' directory
'''
def get_old_puzzles():
    files = os.listdir('data')

    names = {}
    for file in files:
        name = re.findall('[A-Z][^A-Z]*', file)[1].replace('.json', '')
        names[str(name)] = file

    # Sorting dates
    names = sorted(names.items(), key = lambda x: datetime.datetime.strptime(x[0], '%B%d,%Y'))

    return names


# GUI for testing demo

# Displays today's puzzle
def display_todays_puzzle():

    try:
        os.system('python3 src/puzzle/main.py')
    except Exception as e:
        print(e)
        sys.exit()

# Displays old puzzles
def display_old_puzzle(filename):

    try:
        files = get_old_puzzles()
        for file in files:
            if file[0] == filename:
                os.system('python3 src/puzzle/main.py data/' + file[1])

    except Exception as e:
        print(e)
        sys.exit()


root = tk.Tk()
root.title('Welcome')

# lEFT
left_pane = tk.PanedWindow()
left_pane.pack(side = tk.LEFT, padx = (10, 10), pady = (20, 20))

# Label
tk.Label(left_pane, text = "Click to get Today's puzzle").pack()

# Button for Today's puzzle
tk.Button(left_pane, text = "Today's puzzle", command = display_todays_puzzle, relief = tk.RAISED).pack()

# ----------------

# RIGHT
right_pane = tk.PanedWindow()
right_pane.pack(side = tk.RIGHT, padx = (10, 10), pady = (20, 20))

# Label
tk.Label(right_pane, text = "Click to display an old puzzle").pack()


# Combobox
dates = []
for date in get_old_puzzles():
    dates.append(date[0])

cb = ttk.Combobox(right_pane, values = dates, state = "readonly")
cb.set("Choose an old puzzle")
cb.pack()

# Button for Combobox
tk.Button(right_pane, text = "Display puzzle", command = lambda: display_old_puzzle(cb.get()), relief = tk.RAISED).pack()

# Loop
root.resizable(False, False)
root.mainloop()
