import sys
import json

from scraper import PuzzleScraper
from gui import GUI
from log_generator import LogGenerator

# Log generator
l_gen = LogGenerator()

# Loading data
data = None
if len(sys.argv) == 2:
    try:
        filename = str(sys.argv[1])
        with open(filename) as f:
            data = json.load(f)
    except Exception as e:
        print('ERROR: ', e)
        sys.exit()
elif len(sys.argv) == 1:
    p_scrp = PuzzleScraper(l_gen)
    data = p_scrp.fetch_puzzle()
else:
    sys.exit()


# TODO: Call clue generator here with data object and
data['generated_clues'] = data['clues']  # <-- assign here

# GUI with data
gui = GUI(l_gen)
gui.render(data)
