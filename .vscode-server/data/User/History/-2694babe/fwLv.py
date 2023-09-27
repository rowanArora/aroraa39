import math
import sys
from scipy.stats import entropy
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sklearn import tree
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

vectorizer = CountVectorizer()

# Helper Functions:
# START

# This first helper method creates an instance of 
# a decision tree and trains it with the parameters.
def train_decision_tree(X_train, y_train, max_depth, criterion):
    # Make the classifier object.
    clf = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth)

# END

"""
Part A:
Write a function load_data which loads the data,
prepocesses it using a vectorizer, and splits
the entire dataset randomly into 70% training,
15% validation, and 15% test examples.
"""
def load_data():
    # Open, process, and split clean_fake.txt.
    fake = open('clean_fake.txt')
    fake = fake.readlines()
    fake = [line.strip() for line in fake]

    # y keeps track of the actual value for the line.
    # These are all False as they are from clean_fake.txt
    y = [False for i in range(len(fake))]

    # Open, process, and split clean_real.txt.
    real = open('clean_real.txt')
    real = real.readlines()
    real = [line.strip() for line in real]

    # y keeps track of the actual value for the line.
    # These are all True as they are from clean_real.txt
    y += [True for i in range(len(real))]

    # Create an array containing all of the news, both real and fake.
    all_news = real + fake

    # Vectorize the array containing all of the news.
    X = vectorizer.fit_transform(all_news)

    # Split X and y into X_train, X_test, y_train, and y_test.
    # test_size = 0.3 because 15% of the data is for tests,
    # and the other 15% of the data is for validation.
    # The rest 70% of the all_news data set goes towards training.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)

    # Split X_test and y_test into X_test, X_val, y_test, y_val.
    # test_size = 0.5 because we previously split our testing values
    # to be 30% of the dataset, but we really need 15% to be testing data,
    # and 15% to be validation data.
    # So, we can simply split the testing data which is already 30% of the dataset
    # into half for the testing set and validation set.
    X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.5, random_state=10)

    # Now, just return our computed values.
    return {
        'X_train': X_train,
        'X_test': X_test,
        'X_val': X_val,
        'y_train': y_train,
        'y_test': y_test,
        'y_val': y_val
    }

"""
Part B:
Write a function select_model which trains the 
decision tree classifier using at least 5 different
values of max_depth, as well as three different 
split criteria (information gain, log loss and 
Gini coefficient), evaluates the performance of each
one on the validation set, and prints the resulting
accuracies of each model. 

You should use DecisionTreeClassifier, but you should 
write the validation code yourself. 

In your solution PDF (hw1_writeup.pdf), include the output 
of this function as well as a plot of the validation 
accuracy vs. max_depth. 

Additionally, for the hyperparameters that achieve the 
highest validation accuracy, report the corresponding test accuracy.
"""
def select_model():
    return 0

# """Part D"""
# def compute_information_gain():
#     return 0


if __name__ == "__main__":

    # Test for Part A
    learning_data = load_data()
    feature_names = vectorizer.get_feature_names_out()
    print(feature_names)

    # Test for Part B

    # Test for Part C

    # Test for Part D