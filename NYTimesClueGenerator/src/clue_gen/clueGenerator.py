from clue_gen.clueChanger import changeClue

'''
	Changing original clue of the whole Puzzle
	
	:param clues - the original clues of the puzzle
'''


def changePuzzle(clues, trace = False):
	across_clues = clues['across']
	down_clues = clues['down']

	print("\n----Generating across clues----\n")
	changed_across_clues = []
	for ac_clue in across_clues:
		clue = ac_clue['clue']
		word = ac_clue['answer']
		num = ac_clue['number']

		print("\n----------------------------------")
		print("*** Searching clue for \"" + str(word) + "\" ***\n")
		found = False
		for i in range(4):
			if i == 0: print("\t---Looking for definitions---\n")
			elif i == 1: print("\t---Looking for synonyms---\n")
			elif i == 2: print("\t---Looking for antonyms---\n")
			elif i == 3: print("\t---Looking for examples---\n")

			new_clue = changeClue(word, clue, i, trace)
			if new_clue['new_clue'] is not None:
				print("\n*** New clue for \"" + str(word) + "\" is found from " + str(new_clue['source']) + " ***")
				changed_across_clues.append({'clue': new_clue['new_clue'], 'answer': word, 'number': num})
				print("----------------------------------\n")
				found = True
				break

		# No new clue cannot be found
		if found is False:
			print("\n*** No new clue can be found for \"" + str(word) + "\" ***")
			print("----------------------------------\n")
			changed_across_clues.append(ac_clue)

	print("\n----Generating down clues----\n")
	changed_down_clues = []
	for down_clue in down_clues:
		clue = down_clue['clue']
		word = down_clue['answer']
		num = down_clue['number']

		print("\n----------------------------------")
		print("*** Searching clue for \"" + str(word) + "\" ***\n")
		found = False
		for i in range(4):
			if i == 0: print("\t---Looking for definitions---\n")
			elif i == 1: print("\t---Looking for synonyms---\n")
			elif i == 2: print("\t---Looking for antonyms---\n")
			elif i == 3: print("\t---Looking for examples---\n")

			new_clue = changeClue(word, clue, i, trace)
			if new_clue['new_clue'] is not None:
				print("\n*** New clue for \"" + str(word) + "\" is found from " + str(new_clue['source']) + " ***")
				print("----------------------------------\n")
				changed_down_clues.append({'clue': new_clue['new_clue'], 'answer': word, 'number': num})
				found = True
				break

		# No new clue cannot be found
		if found is False:
			print("\n*** No new clue can be found for \"" + str(word) + "\" ***")
			print("----------------------------------\n")
			changed_down_clues.append(down_clue)

	# Returning
	return {
			'across': changed_across_clues,
			'down': changed_down_clues
			}