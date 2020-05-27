""" CIS 192 Python Programming
    Do not distribute. Collaboration is NOT permitted.
"""
import pandas as pd
import math
import nltk
import string
from collections import Counter
from nltk.corpus import inaugural
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import RegexpTokenizer

with open('data/raven.txt', 'r') as raven:
    raw_s = raven.readlines()
output = []
for line in raw_s:
    s = ""
    for c in line:
        if (40 < ord(c) < 91) or (96 < ord(c) < 123) or c == " ":
            s += c
    if s != "":
        line = s.split(" ")
        for s in line:
            if s == "":
                line.remove(s)
        output.append(line)
cols = ["text", "of", "nothing", "raven", "chamber"]
df = pd.DataFrame(columns=cols)
for line in output:
    ans = [" ".join(line)]
    for col in cols:
        if col != "text":
            ans.append(int(col in line))
    df.loc[len(df)] = ans
df.to_csv('raven.csv')


def get_tokens(text):
    # text = inaugural.raw('1789-Washington.txt')
    text = text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    return tokens


def tokenize(text):
    tokens = get_tokens(text)
    tokens = [token for token in tokens
              if token not in stopwords.words('english')]
    stemmer = SnowballStemmer(language='english')
    for token in tokens:
        stemmer.stem(token)
    return tokens


def get_bow(document1, document2):
    bow1 = document1.split(' ')  # bag of words for document1
    bow2 = document2.split(' ')  # bag of words for document2
    return set(bow1).union(set(bow2))


def get_word_counts(document, bow):
    return {w: document.split(' ').count(w) for w in bow}


def compute_tf(d, bow):
    return {w: d.get(w)/sum(d.values()) for w in bow}


def compute_idf(documents):
    bow = documents[0]
    idfs = {}
    for w in bow:
        count = 0
        for d in documents:
            if d.get(w) != 0:
                count += 1
        idfs[w] = math.log(len(documents)/count)
    return idfs


def compute_tfidf(document_tf, idfs):
    return {w: document_tf.get(w)*idfs.get(w) for w in document_tf}
