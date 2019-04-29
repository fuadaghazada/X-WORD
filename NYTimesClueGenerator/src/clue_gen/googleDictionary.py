import urllib.request
import json
import unicodedata

URL = 'https://googledictionaryapi.eu-gb.mybluemix.net/'

'''
	Searching the word in Google Dictionary API (unofficial)
	
	:param word - the given word
'''


def getWordFromGoogleDictionary(word, trace = False):
	# Trace
	if trace is True:
		print("\t\tChecking Google dictionary for the word: \"" + word + "\"")

	# Replacing non-eng chars
	word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf8')

	url = URL + '?define=' + word + '&lang=en'

	meanings = []

	try:
		request = urllib.request.Request(url)
		response = urllib.request.urlopen(request)
		content = response.read().decode('utf-8')
		contentJson = json.loads(content)

		for res in contentJson:
			meaning = res['meaning']

			for key in meaning.keys():
				for definition in meaning[key]:
					meanings.append(definition['definition'])

	except Exception as e:
		pass

	# Trace
	if trace is True and len(meanings) == 0:
		print("\t\tNo results from Google dictionary for the word: \"" + word + "\"\n")

	# Returning word
	word = {
		"word": word,
		"syn": [],
		"ant": [],
		"def": meanings,
		"examples": []
	}

	return word


# TEST
# print(getWordFromGoogleDictionary('İSN\'T'))

