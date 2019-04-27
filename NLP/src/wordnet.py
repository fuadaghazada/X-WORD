from nltk.corpus import wordnet

'''
	For a given word function returns its (if exists):
		* synonym set
		* antonyms
		* definition
		* example sentences
		
	:param str word - the given word
	:return dict result - result object 
'''


def search_wordnet(word):
	# Synonym set of the word)
	synset = wordnet.synsets(str(word))

	synonyms, antonyms = [], []
	definitions, examples = [], []

	for syn in synset:
		for l in syn.lemmas():
			synonyms.append(l.name())
			if l.antonyms():
				antonyms.append(l.antonyms()[0].name())

		definitions.append(syn.definition())
		examples += syn.examples()

	# Removing the duplicates and the word itself
	synonyms = list(set(synonyms))
	if len(synonyms) != 0 and word in synonyms:
		synonyms.remove(word)

	return {
		"word": word,
		"syn": synonyms,
		"ant": antonyms,
		"def": definitions,
		"examples": examples
	}


# TEST
# result = search_wordnet("Good")
# print(result['syn'], '\n')
# print(result['ant'], '\n')
# print(result['def'], '\n')
# print(result['examples'], '\n')

