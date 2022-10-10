"""
Driver for assignment 2 'Word Importance' problems 1 - 3

Author: KLN
Date: Oct 10, 2022
"""
import pandas as pd
from word_importance import word_count
from word_importance import intersection, difference
from word_importance import list_to_dtm, cosine_similarity
from numpy.random import randint
from numpy import zeros


def get_horoscopes(fname):
    """ Extract horoscope-clean column

    Input 
        fname: (str) path to file 
    """
    df = pd.read_csv(fname)

    return df['horoscope-clean'].values


def problem_1(fname):
    data = get_horoscopes(fname)
    text = ' '.join(data)
    wc1 = list(word_count(text).keys())[:100]
    wc2 = list(word_count(text, stopword=False).keys())[:100]
    print('the intersection is for horoscopes with and without stopwords is:')
    for word in intersection(wc1, wc2):
        print(word)


def problem_2(fname, sign1='virgo', sign2='scorpio'):
    df = pd.read_csv(fname)
    idxs1 = df['sign'] == sign1
    idxs2 = df['sign'] == sign2
    texts1 = ' '.join(df['horoscope-clean'].loc[idxs1].values)
    texts2 = ' '.join(df['horoscope-clean'].loc[idxs2].values)
    wc1 = list(word_count(texts1).keys())[:100]
    wc2 = list(word_count(texts2).keys())[:100]
    print(f"the asymmetrical difference of {sign1} to {sign2}")
    for word in difference(wc1, wc2):
        print(word)

def problem3(fname, n=6):
    data = get_horoscopes(fname)
    idxs = randint(low=0, high= len(data), size=n)
    texts = list()
    for idx in idxs:
        texts.append(data[idx])
    
    dtm, lexicon = list_to_dtm(texts)
    D = zeros((n,n))
    for (i, source) in enumerate(dtm):
        for (j, target) in enumerate(dtm):
            #print(i,j,cosine_similarity(source, target))
            D[i,j] = cosine_similarity(source, target)
    print(f'Similarity matrix between {n} documents')
    print(D)
        
    
def main():
    print('[INFO] Solutions for assignment 2')
    filename = 'dat/horoscopes.csv'
    
    # solution to problem 1 with an intersection
    problem_1(filename)
    print()
    # solution to problem 2 with a difference
    problem_2(filename)
    print()
    # solution to problem 3
    problem3(filename)

if __name__=="__main__":
    main()