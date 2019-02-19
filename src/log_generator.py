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
    def __init__(self, filename = None):

        try:
            if filename is None:
                filename = str(datetime.now()).replace(' ', '+')

            filename = os.getcwd() + '/log/' + filename + '.txt'

            if '/src' in filename:
                filename = filename.replace("/src", '')

            self.file = open(str(filename), 'w')

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
