#!/usr/bin/env python3
# Script that uses pandas lib to understand data in a csv file.
# Example usage: ./csv_explore.py --file foo_bar.csv --command headers 
import sys
import argparse
import pandas
import numpy

cmd_choices = ['headers', 'uniq', 'random']
col_cmd_choices = ['uniq']

def main(args):
    e = CsvExplore()
    e.exec()

class CsvExplore():
    filename = None
    command = None
    column = None
    sep = None
    rand_count = None

    def __init__(self):
        parser = argparse.ArgumentParser(description='Uses pandas to explore a csv file.')
        parser.add_argument('--file', required=True, help='Relative path of the file you want to explore')
        parser.add_argument('--command', required=True, help='A command to run on the file', choices=cmd_choices)
        parser.add_argument('--column', help='Required only if using a column command, e.g. uniq')
        args = parser.parse_args()

        self.sep = ','
        self.rand_count = 100
        self.rand_state = numpy.random.RandomState()
        self.filename = args.file
        self.command = args.command
        self.column = args.column
        self.filename = args.file
        self.command = args.command
    
    def exec(self):
        if self.command == 'uniq':
            if self.column is None:
                print("Please provide a column with --column flag")
                sys.exit()
            self.exec_uniq()
        elif self.command == 'headers':
            self.exec_headers()
        elif self.command == 'random':
            self.exec_random_rows()
        
    def exec_random_rows(self):
        d = pandas.read_csv(self.filename, sep=self.sep)
        rand_rows = d.sample(n=self.rand_count, random_state=self.rand_state)
        output_file = self.filename + '.random'
        self.write_to_csv(rand_rows, output_file)
        print(f'File located at {output_file}')

    def exec_uniq(self):
        d = pandas.read_csv(self.filename, sep=self.sep)
        print(d[self.column].unique())

    def exec_headers(self):
        d = pandas.read_csv(self.filename)
        print(d.columns.values.tolist())

    def write_to_csv(self, df, file_name):
        df.to_csv(file_name, sep=',', index_label='index')

if __name__ == '__main__':
    main(sys.argv)
