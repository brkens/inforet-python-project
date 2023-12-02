import numpy as np
import pandas as pd
import csv
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

with open('dblp-v10_sample.csv', newline='') as csvfile:
    mycsvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in mycsvreader:
        abstract = row[0]
        authors = row[1]
        n_citation = row[2]
        references = row[3]
        title = row[4]
        venue = row[5]
        year = row[6]
        id = row[7]
        word = nltk.word_tokenize(id)
        print(word)