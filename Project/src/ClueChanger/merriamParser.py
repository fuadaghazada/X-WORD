import urllib.request
import json

app_key = "5a8472e0-77c3-4e2f-867d-b1fa6f4965b0"
def getWordFromOxford(word):
                url = "https://dictionaryapi.com/api/v3/references/thesaurus/json/"+word+"?key="+app_key
                request = urllib.request.Request(url)
                response = urllib.request.urlopen(request)
                content = response.read().decode('utf-8');
                #print(content)
                contentJson = json.loads(content)
                #print("syns: \n")
                synsMixed = []
                antsMixed = []
                exMixed = []
                defsMixed = []                
                for i in contentJson:
                        meta = i["meta"]                        
                        if(meta["id"] == word):
                                #print("----meta----")
                                #print(meta)
                                syns = meta["syns"]
                                for j in syns:
                                        synsMixed.extend(j)
                                ants = meta["ants"]
                                for j in ants:
                                        antsMixed.extend(j)
                        shortDef = i["shortdef"]
                        defsMixed.extend(shortDef)
                        #print("---Short def-----")
                        #print(shortDef)
                        #print("----Def----")
                        #defs = i["def"]
                        #print(defs)
                #print("---Syns---")                
                #print(synsMixed)
                #print("---Ants---")
                #print(antsMixed)
                word = []
                word.append(synsMixed)
                word.append(defsMixed)
                word.append(exMixed)
                word.append(antsMixed)
                return word
word = getWordFromOxford('above')
for i in word:
        print(i)

