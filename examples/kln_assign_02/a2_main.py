"""
Title: Assignment 2.1-3 Word Importance
Author: Kristoffer Nielbo
Date: 10-10-2022

This script contains the solutions for problems 1-3 from assignment 2.
For problem-specification see README

"""
# dependencies
# Python libraries
import pandas as pd  # data handling
from numpy.random import randint  # number generation
from numpy import zeros  # array generation
# Custom module for information retrieval operations
from word_importance import word_count  # counting word occurrences in texts
from word_importance import intersection, difference  # counting intersection/differences between lists
from word_importance import list_to_dtm, cosine_similarity  # generate document-term matrix and compute cosine similarity between lists


def get_horoscopes(fname):
    """ Extract horoscope-clean column

    Input 
        fname: (str) path to file
    Output
        table: (df) with clean horoscopes 
    """
    df = pd.read_csv(fname)

    return df['horoscope-clean'].values


def problem_1(fname):
    """ Extract intersection of the 100 most likely words in horoscopes
    with and without stopword

    Input 
        fname: (str) path to file
    Output
        NA 
    """
    data = get_horoscopes(fname)
    text = ' '.join(data)
    wc1 = list(word_count(text).keys())[:100] 
    wc2 = list(word_count(text, stopword=False).keys())[:100]
    print('the intersection is for horoscopes with and without stopwords is:')
    for word in intersection(wc1, wc2):
        print(word)


def problem_2(fname, sign1='virgo', sign2='scorpio'):
    """ Extract assymetrical difference between the 100 most likely words for two signs

    Input 
        fname: (str) path to file
        sign1: (str), name of first sign to be compared, default: 'virgo'
        sign2: (str) name of second sign to be compared, default: 'scope'
    Output
        NA 
    """
    df = pd.read_csv(fname)
    idxs1 = df['sign'] == sign1  # subsetting dataframe with boolean indexing
    idxs2 = df['sign'] == sign2
    texts1 = ' '.join(df['horoscope-clean'].loc[idxs1].values)  # join horoscopes to one string
    texts2 = ' '.join(df['horoscope-clean'].loc[idxs2].values)
    wc1 = list(word_count(texts1).keys())[:100]  # extract top 100
    wc2 = list(word_count(texts2).keys())[:100]
    print(f"the asymmetrical difference of {sign1} to {sign2}")
    for word in difference(wc1, wc2):
        print(word)


def problem3(fname, n=6):
    """ Generate a document-term matrix from horocopes and measure distance between n documents 
    using a distance matrix

    Input 
        fname: (str) path to file
        n: (int) number of documents to be compared, default: 6
        Output
        NA 
    """
    data = get_horoscopes(fname)
    idxs = randint(low=0, high= len(data), size=n)  # genrate n random indices for data
    texts = list()
    # extract n random documents
    for idx in idxs:
        texts.append(data[idx])
     
    dtm, _ = list_to_dtm(texts) # generate matrix
    D = zeros((n, n))  # initiate empty distance matrix
    for (i, source) in enumerate(dtm):  # iterate over source document i in D 
        for (j, target) in enumerate(dtm):  # iterate over target document i in D
            D[i, j] = cosine_similarity(source, target)  # compute distance of source and target in D
    print(f'Similarity matrix between {n} documents')  # print result
    print(D)
        
    
def main():
    print('[INFO] Solutions for assignment 2')
    filename = 'dat/horoscopes.csv'
    
    # solution to problem 1 with an intersection
    print('[INFO] Solutions for problem 2.1')
    problem_1(filename)
    print()
    # solution to problem 2 with a difference
    print('[INFO] Solutions for problem 2.2')
    problem_2(filename)
    print()
    # solution to problem 3
    print('[INFO] Solutions for problem 2.3')
    problem3(filename)


if __name__ == "__main__":
    main()