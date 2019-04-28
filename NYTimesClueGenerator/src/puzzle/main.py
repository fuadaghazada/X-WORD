import sys
import json

from puzzle.scraper import PuzzleScraper
from puzzle.gui import GUI
from util.log_generator import LogGenerator

from clue_gen.clueGenerator import changePuzzle

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

# NEW CLUES
data['generated_clues'] = changePuzzle(data['clues'])

# GUI with data
gui = GUI(l_gen)
gui.render(data)
