#!/usr/bin/env python3
# Script that uses scikit-learn lib to perform machine learning tasks and algorithms.
# Example Usage: $ ./machine_learning.py --train_file data.csv.train --test_file data.csv.test --x_col "col_a,col_b" --y_col col_target

import sys
import argparse
import sklearn
import pandas

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main(args):
    ml = ML()
    ml.exec()

class ML():
    train_file = None
    test_file = None
    y_col = None
    x_cols = None

    def __init__(self):
        parser = argparse.ArgumentParser(description='Uses sklearn for ML tasks.')
        parser.add_argument('--train_file', required=True, help='Relative path of the training file for an algorithm')
        parser.add_argument('--test_file', required=True, help='Relative path of the test file for prediction')
        parser.add_argument('--x_cols', required=True, help='List of independent variable column names')
        parser.add_argument('--y_col', required=True, help='Dependent variable column name')
        args = parser.parse_args()

        self.train_file = args.train_file
        self.test_file = args.test_file
        self.y_col = args.y_col
        self.x_cols = [col for col in args.x_cols.split(',')]

    def exec(self):
        # Model training step:
        model = DecisionTreeClassifier()
        df_train = pandas.read_csv(self.train_file, index_col='index')
        model.fit(df_train[self.x_cols], df_train[self.y_col])

        # Model testing step:
        df_test = pandas.read_csv(self.test_file, index_col='index')
        y_predict = model.predict(df_test[self.x_cols])
        model_score = accuracy_score(df_test[self.y_col], y_predict)
        print(model_score)


if __name__ == '__main__':
    main(sys.argv)
