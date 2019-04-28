import requests
import json


APP_ID = 'dfe4face'
APP_KEY = 'c2df8098d116ba55a543ac4fc5f194a0'

LANGUAGE = 'en'
URL = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + LANGUAGE + '/'


def getWordFromOxford(word):
    url = URL + word.lower()

    synsMixed = []
    antsMixed = []
    exMixed = []
    defsMixed = []

    try:
        r = requests.get(url, headers = {'app_id' : APP_ID, 'app_key' : APP_KEY})
        contentJson = json.loads(r.text)

        for result in contentJson['results']:
            lexical_entries = result['lexicalEntries']

            for lex_entr in lexical_entries:
                entries = lex_entr['entries']

                for ent in entries:
                    senses = ent['senses']

                    for sense in senses:
                        defsMixed += sense['definitions']
                        defsMixed += sense['shortDefinitions']
                        defsMixed += sense['examples']

    except Exception as e:
        synsMixed = []
        antsMixed = []
        exMixed = []
        defsMixed = []

    # Returning word
    word = {
        "word": word,
        "syn": synsMixed,
        "ant": antsMixed,
        "def": defsMixed,
        "examples": exMixed
    }

    return word
