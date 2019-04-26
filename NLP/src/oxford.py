# for more information on how to install requests
# http://docs.python-requests.org/en/master/user/install/#install
import requests
import json

# TODO: replace with your own app_id and app_key
app_id = 'dfe4face'
app_key = 'c2df8098d116ba55a543ac4fc5f194a0'

language = 'en'
word_id = 'Ace'

url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

print("code {}\n".format(r.status_code))
print("text \n" + r.text)

print("json \n" + json.dumps(r.json()))


def getWordFromOxford(word):
    app_id = 'dfe4face'
    app_key = 'c2df8098d116ba55a543ac4fc5f194a0'
    language = 'en'
    word_id = word
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()
    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})# the response
    
    contentJson = json.dumps(r.json()) # contents in json
    
    exMixed = []
    defsMixed = []
    for i in contentJson:
     
        #Extracting example sentences
        definition = i["definitions"]
        sseq = definition[0]["sseq"]
        dt=sseq[0][0][1]["dt"]
        example = dt[1][1][0]["t"]
        exMixed.append(example)
        
        #Extracting definitions
        shortDef = i["shortdef_definitions"]
        defsMixed.extend(shortDef)
        
    #Returning word
    word = {
        "def": defsMixed,
        "examples": exMixed
    }

    return word