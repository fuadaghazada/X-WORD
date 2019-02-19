import os
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
            # Writing log to txt format to the file with date name in 'data' folder or project dir
            filename = os.getcwd() + '/log/' + str(datetime.now()).replace(' ', '+') + '.txt'

            if '/src' in filename:
                filename = filename.replace("/src", '')
                
            self.file = open(filename, 'w')

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
