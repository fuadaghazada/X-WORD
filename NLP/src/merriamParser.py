import urllib.request
import json

merriam_app_key = "5a8472e0-77c3-4e2f-867d-b1fa6f4965b0"
def getWordFromOxford(word):
    url = "https://dictionaryapi.com/api/v3/references/thesaurus/json/"+word+"?key="+merriam_app_key
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8');
    contentJson = json.loads(content)
    synsMixed = []
    antsMixed = []
    exMixed = []
    defsMixed = []
    for i in contentJson:
        meta = i["meta"]
        if(meta["id"] == word):
            #Extracting syns and ants
            syns = meta["syns"]
            for j in syns:
                    synsMixed.extend(j)
            ants = meta["ants"]
            for j in ants:
                    antsMixed.extend(j)
            #Extracting example sentences
            definition = i["def"]
            sseq = definition[0]["sseq"]
            dt=sseq[0][0][1]["dt"]
            example = dt[1][1][0]["t"]
            exMixed.append(example)
        #Extracting definitions
        shortDef = i["shortdef"]
        defsMixed.extend(shortDef)
    #Returning word
    word = {
        "syn": synsMixed,
        "ant": antsMixed,
        "def": defsMixed,
        "examples": exMixed
    }

    return word


word = getWordFromOxford('above')
print(word)