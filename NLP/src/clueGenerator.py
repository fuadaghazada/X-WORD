from random import shuffle

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Resources
from wordnet import search_wordnet
from merriamParser import getWordFromMerriam
from urbanParser import getWordFromUrban
from didyoumean import did_you_mean

# All resources to be searched
RESOURCES = [{'name': 'Wordnet', 'func': search_wordnet},
			 {'name': 'Merriam', 'func': getWordFromMerriam},
			 {'name': 'Urban', 'func': getWordFromUrban}]

# For finding the stem (root) of the word
ps = PorterStemmer()

'''
	Changing the given word with its original clue
	according to the given replace policy:
	
	:param str word - the given word
	:param str clue - the original clue for the given word
	:param int replace_policy: 
				0 -> definition
				1 -> synonym
				2 -> antonym
				3 -> example sentence
	:return the given word + the new clue + source of new clue
'''


def changeClue(word, clue, replace_policy):

	# Checking the word in Google's 'Did You Mean'
	did_you_mean_result = did_you_mean(word)
	if did_you_mean_result is not None:
		word = did_you_mean_result

	# Getting the stem of the word
	word = ps.stem(word)

	# Replace policy
	if replace_policy == 0:
		replaced = 'def'
	elif replace_policy == 1:
		replaced = 'syn'
	elif replace_policy == 2:
		replaced = 'ant'
	else:
		replaced = 'examples'

	# New Clue
	new_clue = None
	is_found = False
	source = None

	# Checking the resources
	for resource in RESOURCES:
		results = resource['func'](word)[replaced]

		if results is not None and len(results) != 0:
			# If the original clue returned as a new clue
			if clue in results:
				results.remove(clue)

			# Shuffling for randomness
			shuffle(results)

			for result in results:
				# If definition contains the word itself
				if replaced == 'def' and (word in word_tokenize(result.lower())):
					continue
				# If policy wants example sentence
				elif replaced == 'examples':
					if word not in result.lower():
						continue
					else:
						new_clue = result.lower().replace(word, '...')
						is_found = True
						break
				else:
					new_clue = result
					is_found = True
					break

		# Found
		if is_found is True:
			source = resource['name']
			break

	# Returning
	return {
		'word': word,
		'newclue': new_clue,
		'source': source
	}


# Test
print(changeClue('cars', 'a conveyance for passengers or freight on a cable railway', 0))