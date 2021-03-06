# -*- coding: utf-8 -*-
"""Copy of Data_Analytics_13313162.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lPX-0i5CKpBQGD6nYtnmcJB_cJoNd9WE

#Import Required Python Libraries
"""

import pandas as pd
import numpy as np

"""#Data Prepration"""

# Loading The Dataset

df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/zoo/zoo.data',
                 names=['animal_name', 'hair', 'feathers', 'eggs', 'milk', 'airbone', 'aquatic', 'predator', 'toothed',
                        'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize',
                        'Animal_Type', ])

# Drop The Unnecessary Columns

df = df.drop('animal_name', axis=1)

# Printing The First 10 Rows of The Dataset

print(df.head(10))

df.info()

"""#Data Splitting"""


# Function to split the data into training and testing sets

def train_test_split(df):
    training_data = df.iloc[:90].reset_index(drop=True)  # 90% rows as training data
    testing_data = df.iloc[30:].reset_index(drop=True)  # 30% rows as testing data
    return training_data, testing_data


training_data = train_test_split(df)[0]
testing_data = train_test_split(df)[1]

"""#Entropy"""


# Function to Calculate the Entropy

def calculate_entropy(target_column):
    histogram = np.bincount(target_column)
    ps = histogram / len(target_column)
    result = -np.sum([p * np.log2(p) for p in ps if p > 0])
    return result


"""#Information Gain"""


# Function to Calculate the Information Gain

def Information_Gain(data, split_attribute_name, target_name="Animal_Type"):
    # Calculation of the Total Entropy
    total_entropy = calculate_entropy(data[target_name])

    # Calculation of Split Counts and Values for the Attribure
    values, counts = np.unique(data[split_attribute_name], return_counts=True)

    # Calculation of Weighted Entropy
    weighted_entropyropy = np.sum([(counts[i] / np.sum(counts)) * calculate_entropy(
        data.where(data[split_attribute_name] == values[i]).dropna()[target_name]) for i in range(len(values))])

    # Calculation of Information Gain
    Information_Gain = total_entropy - weighted_entropyropy

    return Information_Gain


"""#Decision Tree Algorithm"""


# ID3 Decision Tree Algorithm

def decision_tree_algorithm(data, original_data, features, target_attribute_name="Animal_Type", parent_node_class=None):
    # Statement to terminate the algorithm and return the leaf node
    if len(np.unique(data[target_attribute_name])) <= 1:
        return np.unique(data[target_attribute_name])[0]

    # Returns the feature value from the original data if the training data is no row of data
    elif len(data) == 0:
        return np.unique(original_data[target_attribute_name])[
            np.argmax(np.unique(original_data[target_attribute_name], return_counts=True)[1])]

    # Returns the parent node if the current node has no features
    elif len(features) == 0:
        return parent_node_class

    # Tree Building Statements
    else:
        parent_node_class = np.unique(data[target_attribute_name])[
            np.argmax(np.unique(data[target_attribute_name], return_counts=True)[1])]

        # Calculating the best split using information gain
        item_values = [Information_Gain(data, feature, target_attribute_name) for feature in features]

        # Calculating Information Gain and Features
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]

        # Tree Creation
        tree = {best_feature: {}}

        features = [i for i in features if i != best_feature]

        # Recursive Tree
        for value in np.unique(data[best_feature]):
            value = value
            sub_data = data.where(data[best_feature] == value).dropna()
            subtree = decision_tree_algorithm(sub_data, df, features, target_attribute_name, parent_node_class)
            tree[best_feature][value] = subtree

        return (tree)


"""#Prediction & Testing"""


# Function for Prediction

def predict_data(query, tree, default=1):
    # Match each feature in query
    for key in list(query.keys()):
        if key in list(tree.keys()):

            try:
                result = tree[key][query[key]]
            except:
                return default

            result = tree[key][query[key]]

            if isinstance(result, dict):
                return predict_data(query, result)

            else:
                return result


# Function to test the data

def test_data(data, tree):
    # Converting the targeted column in dictionary format
    queries = data.iloc[:, :-1].to_dict(orient="records")

    # To store the predicted data
    predicted = pd.DataFrame(columns=["predicted"])

    # To calculate the accuracy of the prediction
    for i in range(len(data)):
        predicted.loc[i, "predicted"] = predict_data(queries[i], tree, 1.0)
    print('The Accuracy of Algorithm is : ', (np.sum(predicted["predicted"] == data["Animal_Type"]) / len(data)) * 100,
          '%')


"""#Run Decision Tree Algorithm"""

tree = decision_tree_algorithm(training_data, training_data, training_data.columns[:-1])
test_data(testing_data, tree)


print(testing_data)


output_data = pd.DataFrame(testing_data, columns= ['hair', 'feathers', 'eggs', 'milk', 'airbone', 'aquatic', 'predator', 'toothed',
                        'backbone', 'breathes', 'venomous', 'fins', 'legs', 'tail', 'domestic', 'catsize',
                        'Animal_Type',])
df.to_csv (r'/Users/abhinav/Desktop/Data/ZOO.csv', index = False, header=True)