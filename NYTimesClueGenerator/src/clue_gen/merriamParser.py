import urllib.request
import json

merriam_app_key = "5a8472e0-77c3-4e2f-867d-b1fa6f4965b0"

'''
    Parsing the given word from Merriam Dictionary API

    :param word - the given word
'''


def getWordFromMerriam(word, trace = False):
    # Trace
    if trace is True:
        print("\t\tChecking Merriam dictionary for the word: \"" + word + "\"")

    url = "https://dictionaryapi.com/api/v3/references/thesaurus/json/"+word+"?key="+merriam_app_key
    synsMixed = []
    antsMixed = []
    exMixed = []
    defsMixed = []
    try:
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        contentJson = json.loads(content)
        for i in contentJson:

                meta = i["meta"]
                if(meta["id"] == word):
                    # Extracting syns and ants
                    syns = meta["syns"]
                    for j in syns:
                            synsMixed.extend(j)
                    ants = meta["ants"]
                    for j in ants:
                            antsMixed.extend(j)
                    # Extracting example sentences
                    definition = i["def"]
                    sseq = definition[0]["sseq"]
                    dt=sseq[0][0][1]["dt"]
                    example = dt[1][1][0]["t"]
                    example = example.replace('{it}', '').replace('{/it}', '')
                    exMixed.append(example)
                # Extracting definitions
                shortDef = i["shortdef"]
                defsMixed.extend(shortDef)
    except Exception as e:
        synsMixed = []
        antsMixed = []
        exMixed = []
        defsMixed = []

    # Trace
    if trace is True and len(synsMixed) == 0  and len(antsMixed) == 0 and len(defsMixed) == 0 and len(exMixed) == 0:
        print("\t\tNo results from Merriam dictionary for the word: \"" + word + "\"\n")

    # Returning word
    word = {
        "word": word,
        "syn": synsMixed,
        "ant": antsMixed,
        "def": defsMixed,
        "examples": exMixed
    }

    return word

