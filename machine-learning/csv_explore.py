#!/usr/bin/env python3
# Script that uses pandas lib to understand data in a csv file.
# Example usage: ./csv_explore.py --file data.csv --command headers 
import sys
import argparse
import pandas
import numpy

cmd_choices = ['headers', 'uniq', 'random', 'create_sets']
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
        self.rand_frac = .20
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
        elif self.command == 'create_sets':
            self.exec_create_sets()
        
    def exec_random_rows(self):
        df, rand_rows = self.get_rand_rows()
        output_file = self.filename + '.random'
        self.write_to_csv(rand_rows, output_file)
        print(f'File located at {output_file}')

    def exec_uniq(self):
        d = pandas.read_csv(self.filename, sep=self.sep)
        values = numpy.sort(d[self.column].unique())
        for v in values:
            print(v)

    def exec_headers(self):
        d = pandas.read_csv(self.filename)
        print(d.columns.values.tolist())

    def exec_create_sets(self):
        df, test_rows = self.get_rand_rows()
        train_rows = df.drop(test_rows.index)
        self.write_to_csv(test_rows, self.filename + '.test')
        self.write_to_csv(train_rows, self.filename + '.train')

    def get_rand_rows(self):
        df = pandas.read_csv(self.filename, sep=self.sep)
        return df, df.sample(frac=self.rand_frac, replace=False, random_state=self.rand_state)

    def write_to_csv(self, df, file_name):
        df.to_csv(file_name, sep=',', index_label='index')

if __name__ == '__main__':
    main(sys.argv)
