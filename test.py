import json
from pprint import pprint

with open('data/Monday February 11, 2019.json') as f:
    data = json.load(f)
    pprint(data)
