import sys
import json

from scraper import fetch_puzzle
from gui import render

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
    data = fetch_puzzle()
else:
    sys.exit()

# GUI with data
render(data)
