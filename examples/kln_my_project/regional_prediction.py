"""
Title: regional prediction of the world happiness survey
Author: Kristoffer Nielbo
Date: 10-10-2022

This script trains a classifier to predict region from world happiness and related predictors
for the problem-specification see README

"""
# Python libraries
import pandas as pd  # data handling
from sklearn.model_selection import train_test_split  # data splitting
from sklearn.linear_model import LogisticRegression  # model training


def main():
    
    fname = 'dat/world-happiness-report-2021.dat'
    print(f'[INFO] reading and preprocessing {fname}...')
    df = pd.read_csv(fname)
    X = df.iloc[:,[2,6,7,8,9,10,11]]  # extract relevant features
    y = df.iloc[:,1]
    print(y)
    # print column names
    for (i, colname) in enumerate(X.columns):
        print(f'feature {i}: {colname}')
    
    # split in training and test data sets
    training_size = 0.15
    print(f'[INF0] splitting in train/test: {str(1-training_size)+"/"+str(training_size)}')
    X_train, X_test, y_train, y_test = train_test_split(
        X, 
        y, 
        test_size=0.15, 
        random_state=23
        )
    
    # train classifier
    print('[INFO] training classifier...')
    clf = LogisticRegression(max_iter=10000, random_state=0,multi_class='multinomial')
    clf.fit(X_train, y_train)

    # predictive performance
    print(f'[INFO] predictive performance (mean ACC) on test set: {clf.score(X_test, y_test)}')

    # print coefficients for trained classifier for each class for each predictor
    for i in range(len(clf.classes_)):
        print(clf.classes_[i])
        for j in range(len(X.columns)):
            print('>', X.columns[j])
            print('>>', clf.coef_[i][j])
        print()

if __name__ == '__main__':
    main()