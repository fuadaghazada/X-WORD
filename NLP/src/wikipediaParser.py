import warnings
import wikipedia
from nltk.tokenize import sent_tokenize


'''
	Searching the given word in the Wikipedia
	
	:param str word -  the given word
'''


def search_wikipedia(word):
	# To ignore module warnings
	warnings.filterwarnings('ignore')

	# Example sentences
	sentences = []

	try:
		# Summary of the given word in Wikipedia
		summary_sentences = sent_tokenize(wikipedia.summary(word))

		# Looking for the sentences containing the given word
		for sentence in summary_sentences:
			if word.lower() in sentence.lower():
				sentences.append(sentence)

	except Exception as e:
		pass

	return {
		"word": word,
		"syn": [],
		"ant": [],
		"def": [],
		"examples": sentences
	}