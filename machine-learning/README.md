# A Collection of Machine Learning Utilites

## Install
Run:
```
$ pip3 install -r requirements.txt
```

## Usage
For full documentation, run:
```
$ ./csv_explore.py --help
```
#### Examples

Get headers of a file:
```
$ ./csv_explore.py --file data.csv --command headers
['id', 'name', 'email', 'active']
```

Split data into a training file and a test file:
```
$ ./csv_explore.py --file data.csv --command create_sets
$ ls data.csv.*
data.csv.test   data.csv.train
```

Input a training file and a test file to get a prediction score using DecisionTreeClassifier from [scikit-learn](https://github.com/scikit-learn/scikit-learn).
```
$ ./machine_learning.py --train_file data.csv.train --test_file data.csv.test --x_col "col_a,col_b" --y_col col_target
0.9143
```