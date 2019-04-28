import urllib.request
import json

URL = "http://api.urbandictionary.com/v0/define?term="

'''
    Parsing the given word from Urban Dictionary API
    
    :param word - the given word
'''


def getWordFromUrban(word):
    url = URL + word

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8');
    contentJson = json.loads(content)

    defsMixed = []
    exMixed = []
    list = contentJson["list"]

    for i in list:
        if(i["word"] == word):
            definition = i["definition"]
            defsMixed.append(definition)
            example = i["example"]
            exMixed.append(example)
    word = {
        "word": word,
        "syn": [],
        "ant": [],
        "def": defsMixed,
        "examples": exMixed
    }
    return word
