#!/usr/bin/env python3
# Script that uses pandas lib to understand data in a csv file.
import sys
import pandas as pandas

def main(args):
    print("Starting...")
    e = CsvExplore(args)
    e.exec()
    print("Done")

class CsvExplore():
    filename = None
    column = None

    def __init__(self, args):
        if len(args) == 2:
            self.filename = args[0]
            self.column = args[1]
        else:
            sys.exit("You must supply a file and column name as args.")
    
    def exec(self):
        print(self.filename)
        d = pandas.read_csv(self.filename)
        print(d[self.column].unique())

if __name__ == '__main__':
    main(sys.argv[1:])