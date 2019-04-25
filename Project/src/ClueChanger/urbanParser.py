import urllib.request
import json

def getWordFromUrban(word):
                url = "http://api.urbandictionary.com/v0/define?term=" + word
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
                word = []
                word.append(defsMixed)
                word.append(exMixed)
                return word
word = getWordFromUrban('test')
for i in word:
    print(i)
