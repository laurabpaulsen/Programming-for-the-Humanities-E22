from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

def main():
    #X, y = load_iris(return_X_y=True)
    dpath = '/home/au215773/CENTRAL/DEVTEAM/EDUX/programming-for-the-humanities/pfth22/dat/world-happiness-report-2021.dat' 
    print(f'[INFO] Preparing data...')
    df = pd.read_csv(dpath)
    df = df.iloc[:, :13]
    print(df.shape)
    print(df.columns)
    #X = df.loc[:,['Regional indicator', 'Perceptions of corruption']].values
    X = df.iloc[:,[1,6,7,8,9,10,11]]
    print(X.columns)
    #x = X[:,1].reshape(-1,1)
    x = X.iloc[:,1:]
    print(x)
    
    y = X.iloc[:,0]#.reshape(-1,1)
    
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, 
        test_size=0.15, 
        random_state=23
        )
    
    clf = LogisticRegression(max_iter=10000, random_state=0,multi_class='multinomial')
    
    clf.fit(X_train, y_train)
    
    
    print(clf.predict(X_test))
    print(y_test)
    #print(clf.predict_proba(x))
    print(clf.score(X_test, y_test))
    
    print(clf.classes_)
    print(clf.coef_)
    print(X.columns)
    
if __name__=='__main__':
    main()





