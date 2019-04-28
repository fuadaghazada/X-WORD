from clue_gen.clueChanger import changeClue

'''
	Changing original clue of the whole Puzzle
	
	:param clues - the original clues of the puzzle
'''


def changePuzzle(clues):
	across_clues = clues['across']
	down_clues = clues['down']

	print("\n----Generating across clues----\n")
	changed_across_clues = []
	for ac_clue in across_clues:
		clue = ac_clue['clue']
		word = ac_clue['answer']
		num = ac_clue['number']

		print("Searching clue for \"" + str(word) + "\"")
		found = False
		for i in range(4):
			new_clue = changeClue(word, clue, i)
			if new_clue['new_clue'] is not None:
				print("New clue for \"" + str(word) + "\" is found from " + str(new_clue['source']) + "\n")
				changed_across_clues.append({'clue': new_clue['new_clue'], 'answer': word, 'number': num})
				found = True
				break

		# No new clue cannot be found
		if found is False:
			print("No new clue cannot be found for \"" + str(word) + "\"\n")
			changed_across_clues.append(ac_clue)

	print("\n----Generating down clues----\n")
	changed_down_clues = []
	for down_clue in down_clues:
		clue = down_clue['clue']
		word = down_clue['answer']
		num = down_clue['number']

		print("Searching clue for \"" + str(word) + "\"")
		found = False
		for i in range(4):
			new_clue = changeClue(word, clue, i)
			if new_clue['new_clue'] is not None:
				print("New clue for \"" + str(word) + "\" is found from " + str(new_clue['source']) + "\n")
				changed_down_clues.append({'clue': new_clue['new_clue'], 'answer': word, 'number': num})
				found = True
				break

		# No new clue cannot be found
		if found is False:
			print("No new clue cannot be found for \"" + str(word) + "\"\n")
			changed_down_clues.append(down_clue)

	# Returning
	return {
			'across': changed_across_clues,
			'down': changed_down_clues
			}