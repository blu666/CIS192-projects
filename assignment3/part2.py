"""
    CIS 192 Python Programming
    Do not distribute. Collaboration is permitted with one person.
"""

from collections import defaultdict
import gzip
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier


"""
    Section 0: Data
"""


def load_file(data_file):
    words = []
    labels = []
    with open(data_file, 'r', encoding="utf8") as f:
        i = 0
        for line in f:
            if i > 0:
                line_split = line[:-1].split("\t")
                words.append(line_split[0].lower())
                labels.append(int(line_split[1]))
            i += 1
    return words, labels


def load_ngram_counts(ngram_counts_file):
    counts = defaultdict(int)
    with gzip.open(ngram_counts_file, 'rt') as f:
        for line in f:
            token, count = line.strip().split('\t')
            if token[0].islower():
                counts[token] = int(count)
    return counts


"""
    Section 1: Evaluation Metrics
"""


def get_accuracy(predictions, labels):
    correct = 0
    for i in range(len(predictions)):
        if predictions[i] == labels[i]:
            correct += 1
    return correct/len(predictions)


"""
    Section 2: Baseline Models
"""


def all_complex(test_file):
    words, labels = load_file(test_file)
    predictions = [1]*len(words)
    return get_accuracy(predictions, labels)


def word_length_threshold(train_file, test_file):
    # TODO: write your code here to classify words based on their length
    # and a given threshold. e.g. if the threshold is 9, any words with
    # less than 9 characters will be labeled simple, and any words with 9
    #  characters or more will be labeled complex.

    # Write your code to return the training and testing accuracy score. Your
    # code should find the best length threshold by accuracy, and uses this
    # threshold to classify the training and test set.
    train_words, train_labels = load_file(train_file)
    test_words, test_labels = load_file(test_file)
    max_len = 0
    for word in train_words:
        if len(word) > max_len:
            max_len = len(word)
    max_p = 0
    for i in range(1, max_len):
        predictions = [0 if len(word) < i else 1 for word in train_words]
        p = get_accuracy(predictions, train_labels)
        if p > max_p:
            max_p = p
            threshold = i
    test_predictions = [0 if len(word) < threshold else 1
                        for word in test_words]
    test_performance = get_accuracy(test_predictions, test_labels)
    return max_p, test_performance


def word_frequency_threshold(train_file, test_file, counts):
    # TODO: write your code to return the training and development
    # accuracy score. Your code should find the best frequency threshold by
    # accuracy, and uses this threshold to classify the training
    # and testing set.
    train_words, train_labels = load_file(train_file)
    test_words, test_labels = load_file(test_file)
    train_dict = {}
    for w in train_words:
        if counts.get(w) is None:
            train_dict[w] = 0
        else:
            train_dict[w] = counts.get(w)
    max_p = 0
    for i in list(train_dict.values()):
        predictions = [0 if train_dict.get(word) > i else 1
                       for word in train_words]
        p = get_accuracy(predictions, train_labels)
        if p > max_p:
            max_p = p
            threshold = i
    test_dict = {}
    for w in test_words:
        if counts.get(w) is None:
            test_dict[w] = 0
        else:
            test_dict[w] = counts.get(w)
    # test_dict = {w: counts.get(w) for w in test_words}
    test_predictions = [0 if test_dict.get(word) > threshold else 1
                        for word in test_words]
    development_performance = get_accuracy(test_predictions, test_labels)
    print(threshold)
    return max_p, development_performance


"""
    Section 3: Machine Learning Models
"""


def process_data(train_file, test_file, counts):
    train_words, train_labels = load_file(train_file)
    test_words, test_labels = load_file(test_file)
    train_words_length = [len(w) for w in train_words]
    # train_words_hyphen = [int("-" in w) for w in train_words]
    train_words_freq = []
    for w in train_words:
        if counts.get(w) is None:
            train_words_freq.append(0)
        else:
            train_words_freq.append(counts.get(w))
    X_train = np.column_stack((train_words_length, train_words_freq))
    Y_train = np.asarray(train_labels)

    test_words_length = [len(w) for w in test_words]
    test_words_freq = []
    for w in test_words:
        if counts.get(w) is None:
            test_words_freq.append(0)
        else:
            test_words_freq.append(counts.get(w))
    X_test = np.column_stack((test_words_length, test_words_freq))

    return X_train, Y_train, X_test, train_labels, test_labels


def naive_bayes(train_file, test_file, counts):
    X_train, Y_train, X_test, train_labels, test_labels = \
        process_data(train_file, test_file, counts)

    gnb = GaussianNB()
    gnb.fit(X_train, Y_train)

    train_predict = gnb.predict(X_train)
    test_predict = gnb.predict(X_test)
    train_predict_list = train_predict.tolist()
    test_predict_list = test_predict.tolist()
    training_performance = get_accuracy(train_predict_list, train_labels)
    test_performance = get_accuracy(test_predict_list, test_labels)
    return training_performance, test_performance


def logistic_regression(train_file, test_file, counts):
    X_train, Y_train, X_test, train_labels, test_labels = \
        process_data(train_file, test_file, counts)

    logRegr = LogisticRegression(solver='liblinear')
    logRegr.fit(X_train, Y_train)

    train_predict = logRegr.predict(X_train)
    test_predict = logRegr.predict(X_test)
    train_predict_list = train_predict.tolist()
    test_predict_list = test_predict.tolist()
    training_performance = get_accuracy(train_predict_list, train_labels)
    test_performance = get_accuracy(test_predict_list, test_labels)

    return training_performance, test_performance


def decision_tree(train_file, test_file, counts):
    X_train, Y_train, X_test, train_labels, test_labels = \
        process_data(train_file, test_file, counts)

    dt = DecisionTreeClassifier(max_depth=5)
    dt.fit(X_train, Y_train)

    train_predict = dt.predict(X_train)
    test_predict = dt.predict(X_test)
    train_predict_list = train_predict.tolist()
    test_predict_list = test_predict.tolist()
    training_performance = get_accuracy(train_predict_list, train_labels)
    test_performance = get_accuracy(test_predict_list, test_labels)

    return training_performance, test_performance


def random_forest(train_file, test_file, counts):
    X_train, Y_train, X_test, train_labels, test_labels = \
        process_data(train_file, test_file, counts)

    rfc = RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
    rfc.fit(X_train, Y_train)

    train_predict = rfc.predict(X_train)
    test_predict = rfc.predict(X_test)
    train_predict_list = train_predict.tolist()
    test_predict_list = test_predict.tolist()
    training_performance = get_accuracy(train_predict_list, train_labels)
    test_performance = get_accuracy(test_predict_list, test_labels)

    return training_performance, test_performance


def adaBoost(train_file, test_file, counts):
    X_train, Y_train, X_test, train_labels, test_labels = \
        process_data(train_file, test_file, counts)

    ada = AdaBoostClassifier()
    ada.fit(X_train, Y_train)

    train_predict = ada.predict(X_train)
    test_predict = ada.predict(X_test)
    train_predict_list = train_predict.tolist()
    test_predict_list = test_predict.tolist()
    training_performance = get_accuracy(train_predict_list, train_labels)
    test_performance = get_accuracy(test_predict_list, test_labels)

    return training_performance, test_performance


if __name__ == "__main__":
    train_file = "data/complex_words_training.txt"
    test_file = "data/complex_words_test.txt"

    train_data = load_file(train_file)
    test_data = load_file(test_file)

    # should take around 20 seconds due to size
    ngram_counts_file = "data/ngram_counts.txt.gz"
    counts = load_ngram_counts(ngram_counts_file)
    print("all complex:" + str(all_complex(test_file)))
    print("word length threshold:" +
          str(word_length_threshold(train_file, test_file)))
    print("word freq threshold:" +
          str(word_frequency_threshold(train_file, test_file, counts)))
    print("naive bayes:" + str(naive_bayes(train_file, test_file, counts)))
    print("logistic regression" +
          str(logistic_regression(train_file, test_file, counts)))
    print("decision tree:" + str(decision_tree(train_file, test_file, counts)))
    print("random forest:" + str(random_forest(train_file, test_file, counts)))
    print("AdaBoost:" + str(adaBoost(train_file, test_file, counts)))
