import urllib.request
import json
from pprint import pprint

merriam_app_key = "5a8472e0-77c3-4e2f-867d-b1fa6f4965b0"
def getWordFromMerriam(word):                
                try:
                    url = "https://dictionaryapi.com/api/v3/references/thesaurus/json/"+word+"?key="+merriam_app_key
                    request = urllib.request.Request(url)
                    response = urllib.request.urlopen(request)
                    content = response.read().decode('utf-8');                
                    contentJson = json.loads(content)
                    #pprint(contentJson);
                    #print("syns: \n")
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
                                    example = example.replace("{it}","");
                                    example = example.replace("{/it}","");
                                    exMixed.append(example)
                            #Extracting definitions
                            shortDef = i["shortdef"]
                            defsMixed.extend(shortDef)
                    #Returning word
                    word = {
                        "word":word,
                        "syn":synsMixed,
                        "ant":antsMixed,
                        "def":defsMixed,
                        "example":exMixed
                    }
                    return word
                except Exception as e:
                    print("Exception")
                    word = {
                    "word":word,                    
                    "syn":[],
                    "ant":[],
                    "def":[],
                    "example":[]
                    }
                    return word             
            
def eliminateUnsuitableDefs(word):
    defs = word["def"]        
    for i in range (0,len(defs)):        
        defWords = defs[i].split()        
        for j in defWords:
            print(j+word["word"])
            if (word["word"] in j):
                print(i)
                del defs[i]
                break

def changePuzzle(words,clues):
    replacePolicy = [3,3,3,1]
    newClues = []
    
    for word in words:
        isReplaced = False
        for i in range (0,len(replacePolicy)):
            remaining = replacePolicy[i]

            if(remaining!=0):
                result = changeClue(i)
                #If changeClue succeded
                if(result!=None):
                    replacePolicy[i] = replacePolicy[i]-1
                    isReplaced = True
                    newClues.append(result)
                    break
        if(!isReplaced):
            
word = getWordFromMerriam('sled')
eliminateUnsuitableDefs(word)
print(word["syn"]);
print(word["ant"]);
print(word["def"]);
print(word["example"]);
