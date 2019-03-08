import csv

'''
    Writing the given data in rows to a csv file
'''
def write_to_csv(data):
    with open('../data/result.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(['Puzzle #', '# of moves (beam width 2)', '# of moves (beam width 3)'])
        for row in data:
            writer.writerow(row)

'''
    Writing the puzzles to a text file
'''
def write_to_txt(puzzles):
    with open('../data/puzzles.txt', 'w') as writeFile:
        for puzzle in puzzles:
            for i in puzzle:
                for j in i:
                    writeFile.write(j + '\t')
                writeFile.write('\n')
            writeFile.write('\n')
