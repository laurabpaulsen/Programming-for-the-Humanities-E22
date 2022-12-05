import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler


def standardize(X):
    """ standardize to make beta coefficient equal to Pearson's Rho
    """
    scaler = StandardScaler()
    scaler.fit(X)
    return scaler.transform(X)


def main():
    dpath = '/home/au215773/CENTRAL/DEVTEAM/EDUX/programming-for-the-humanities/pfth22/dat/world-happiness-report-2021.dat' 
    print(f'[INFO] Preparing data...')
    df = pd.read_csv(dpath)
    df = df.iloc[:, :13]
    X = df.loc[:,['Ladder score', 'Perceptions of corruption']].values
    print(f'[INFO] Training regression model')
    ## original values
    #y = df['Ladder score'].values.reshape(-1,1)
    #X = df['Perceptions of corruption'].values.reshape(-1,1)
    ## standardized values
    X_sd = standardize(X)
    x = X_sd[:,1].reshape(-1, 1)
    y = X_sd[:,0].reshape(-1, 1)
    # train-test split

    X_train, X_test, y_train, y_test = train_test_split(
        x, y, 
        test_size=0.25, 
        random_state=23
        )

    ## fit
    print(f'[INFO] Training classification model')    
    reg = linear_model.LinearRegression()
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    print("Coefficients: \n", reg.coef_)
    # The mean squared error
    print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
    # The coefficient of determination: 1 is perfect prediction
    print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))

    x, y = x.ravel(), y.ravel()
    m, b = np.polyfit(x, y, 1)
    fig = plt.figure(figsize=(4,3))
    plt.plot(x, y, 'xg')
    plt.plot(x, m * x + b, 'r')
    plt.xlabel('Perceptions of corruption')
    plt.ylabel('Ladder score')
    plt.tight_layout()
    plt.savefig('fig/happy_on_corrupt.png')

if __name__ == '__main__':
    main()