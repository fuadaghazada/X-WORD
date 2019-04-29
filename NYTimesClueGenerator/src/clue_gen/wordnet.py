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


def search_wordnet(word, trace = False):
	# Trace
	if trace is True:
		print("\t\tChecking Wordnet for the word: \"" + word + "\"")

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
	if len(synonyms) != 0 and word.lower() in synonyms:
		synonyms.remove(word.lower())

	# Trace
	if trace is True and len(synonyms) == 0 and len(antonyms) == 0 and len(definitions) == 0 and len(examples) == 0:
		print("\t\tNo results from Wordnet for the word: \"" + word + "\"\n")

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

