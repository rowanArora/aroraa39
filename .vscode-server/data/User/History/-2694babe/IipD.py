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
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import pandas as pd

vectorizer = CountVectorizer()

# Helper Functions:
# START

# This first helper function creates an instance of 
# a decision tree and trains it with the parameters.
def train_decision_tree(X_train, y_train, max_depth, criterion):
    # Make the classifier object.
    clf = DecisionTreeClassifier(criterion=criterion, max_depth=max_depth)

    # Train the newly created classifier object
    # on the input data.
    clf.fit(X_train, y_train)

    # Return the trained decision tree classifer.
    return clf

# This next helper function makes predictions
# based on the model, X_test dataset, and
# criterion passed in the parameters.
def make_predictions(X_test, model, criterion='gini'):
    # First check to see if the input criterion
    # is either information gain, log loss, or
    # Gini coefficient.
    if criterion == 'log_loss' or criterion == 'entropy' or criterion == 'gini':
        y_prediction = model.predict(X_test)
        return y_prediction
    
# This next helper function measures the accuracy
# of the input model based on the X_test and y_test
# datasets.
def measure_model_accuracy(model, X_test, y_test):
    # We will first call make_predictions() on X_test
    # and the model to get an array of predictions.
    y_predictions = make_predictions(X_test, model)

    # We will then call accuracy score from sklearn.metrics
    # to compare the scores from y_prediction and y_test
    # and see exactly how accurate our predictions were.
    accuracy = accuracy_score(y_test, y_predictions) * 100

    # Then, simply print out the accuracy score and return
    # the value stored in accuracy.
    return accuracy

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
def select_model(learning_data):
    # Let us create a couple local variables to track
    # the maximum accuracy we have achieved and the best
    # classifier we have found.
    max_accurancy = 0
    best_classifier = None

    # Next, we need to find a valid scalar value to multiply
    # against our max_depth value.
    # From lecture, we know we can use the entropy of a random
    # variable to help us determine how to split data.
    # In this case, we are determining the max_depth that the
    # decision tree classifier can reach, so let's use the entropy 
    # equation on the length of X_train.
    max_depth_scalar = int(math.log2(len(learning_data['X_train'].toarray())))

    # Now, we can finally start training our trees using five 
    # different values of max_depth and using three different
    # split criteria.
    # Here are our three different split criteria:
    for criterion in ['gini', 'entropy', 'log_loss']:
        for curr in range(1, 5):
            # Here is our current max_depth value.
            max_dept = curr * max_depth_scalar
            # We call our helper function to make a new instance of the DecisionTreeClassifier
            # and train it on our input data.
            curr_clf = train_decision_tree(learning_data['X_train'], learning_data['y_train'], max_dept, criterion)
            # We then call another helper function to check the accuracy of our trained model.
            curr_accuracy = measure_model_accuracy(curr_clf, learning_data['X_val'], learning_data['y_val'])
            # We then check to see if curr_accuracy is greater than our max_accuracy, and if it is
            # we will update the value of max_accuracy to be equal to curr_accuracy.
            if curr_accuracy > max_accurancy:
                max_accurancy = curr_accuracy
                best_classifier = curr_clf
            # Then, we will print out our curr_accuracy.
            print("The results for the model with the ", criterion, "split criteria, and max depth of ", max_dept, "is:")
            print("\t Accuracy = ", curr_accuracy)
    return max_accurancy, best_classifier

# """Part D"""
# def compute_information_gain():
#     return 0


if __name__ == "__main__":

    # Test for Part A
    learning_data = load_data()
    feature_names = vectorizer.get_feature_names_out()
    print(feature_names)

    # Test for Part B
    accuracy, decision_tree_model = select_model(learning_data)

    # Test for Part C

    # Test for Part D