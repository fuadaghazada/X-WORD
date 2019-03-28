import csv

'''
    Writing the given data in rows to a csv file
'''
def write_to_csv(data):
    with open('../data/result.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(['Puzzle #', '# of moves (BBS)', '# of moves (A*)'])
        for row in data:
            writer.writerow(row)

'''
    Writing the puzzles to a text file in a 'pretty format'
'''
def write_to_txt(puzzles):
    with open('../data/puzzles.txt', 'w') as writeFile:
        index = 1
        for puzzle in puzzles:
            writeFile.write(str(index) + ")\n")
            writeFile.write('-----\n')
            for i in puzzle:
                for j in i:
                    if j is i[0]:
                        writeFile.write('| ')
                    writeFile.write(j + ' | ')
                writeFile.write('\n-------------\n')
            writeFile.write('\n')
            index += 1
