import urllib.request
import json

merriam_app_key = "5a8472e0-77c3-4e2f-867d-b1fa6f4965b0"
def getWordFromOxford(word):
                url = "https://dictionaryapi.com/api/v3/references/thesaurus/json/"+word+"?key="+merriam_app_key
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
                word = []
                word.append(synsMixed)
                word.append(defsMixed)
                word.append(exMixed)
                word.append(antsMixed)
                return word
word = getWordFromOxford('above')
for i in word:
       print(i)
