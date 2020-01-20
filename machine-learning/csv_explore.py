#!/usr/bin/env python3
# Script that uses pandas lib to understand data in a csv file.
# Usage: ./csv_explore.py <file> <command> [<options>...]
import sys
import pandas as pandas

def main(args):
    e = CsvExplore(args)
    e.exec()

class CsvExplore():
    filename = None
    command = None
    column = None
    sep = None
    rand_count = None

    def __init__(self, args):
        self.sep = ','
        self.rand_count = 100
        if len(args) == 3:
            self.filename = args[0]
            self.command = args[1]
            self.column = args[2]
        elif len(args) == 2:
            self.filename = args[0]
            self.command = args[1]
        else:
            sys.exit("You must supply args: \"file command [options]\"")
    
    def exec(self):
        if self.command == 'uniq':
            self.exec_uniq()
        elif self.command == 'headers':
            self.exec_headers()
        elif self.command == 'random':
            self.exec_random_rows()
        
    def exec_random_rows(self):
        d = pandas.read_csv(self.filename, sep=self.sep)
        rand_rows = d.sample(n=self.rand_count)
        self.write_to_csv(rand_rows, self.filename + '.random')

    def exec_uniq(self):
        d = pandas.read_csv(self.filename, sep=self.sep)
        print(d[self.column].unique())

    def exec_headers(self):
        d = pandas.read_csv(self.filename)
        print(d.columns.values.tolist())

    def write_to_csv(self, df, file_name):
        df.to_csv(file_name, sep=',', index_label='index')

if __name__ == '__main__':
    main(sys.argv[1:])
