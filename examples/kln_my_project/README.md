# Solutions to Assignments 2 -- Word Importance #

## Group

* name_1 nameson_1
* name_2 nameson_2

## How to execute

First ensure that the dependencies are installed

```sh
$ pip install -r requirements.txt
```

Then execute the driver

```sh
$ python3 regional_prediction.py
```

## Problem specification

This project uses a multi class logistic regression model to predict the region (`Regional indicator`) from the following 8 features in the World Happiness Survey from 2021:

```sh
feature 0: Ladder score
feature 1: Logged GDP per capita
feature 2: Social support
feature 3: Healthy life expectancy
feature 4: Freedom to make life choices
feature 5: Generosity
feature 6: Perceptions of corruption
```

The features were selected because they are significant point estimates in the survey (additional features are mostly uncertainty estimates). The trained classifier obtains a mean accuracy of 0.52.