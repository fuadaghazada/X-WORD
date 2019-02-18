import sys
from datetime import datetime

'''
    Simple Log generator for tracing the programs
'''
class LogGenerator:

    '''
        Constructor
    '''
    def __init__(self):

        try:

            filename = str(datetime.now()).replace(' ', '+') + ".txt"
            self.file = open('log/' + filename, 'w')

            self.write_to_file('Log file is generated!')

        except Exception as e:
            print('ERROR: Cannot create log file')
            sys.exit()

    '''
        Writing the given 'operation' to the file
    '''
    def write_to_file(self, operation):
        try:
            log = str(datetime.now()) + ': ' + str(operation) + "\n"
            self.file.write(log)
        except Exception as e:
            print('ERROR: Cannot write to log file')
            sys.exit()
