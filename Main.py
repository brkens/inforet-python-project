import numpy as np
import pandas as pd
import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

stemmed_documents = []
lemmatized_documents = []

with open('dblp-v10_sample.csv', newline='') as csvfile:
    mycsvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in mycsvreader:
        words = nltk.word_tokenize(row[0]) # abstract
        words += nltk.word_tokenize(row[1]) # authors
        words += nltk.word_tokenize(row[2]) # n_citation
        words += nltk.word_tokenize(row[3]) # references
        words += nltk.word_tokenize(row[4]) # title
        words += nltk.word_tokenize(row[5]) # venue
        words += nltk.word_tokenize(row[6]) # year
        words += nltk.word_tokenize(row[7]) # id

        stop_words = set(stopwords.words("english"))
        filtered_words = []
        for word in words:
            if word.casefold() not in stop_words:
                filtered_words.append(word)

        # Stemming
        stemmer = PorterStemmer()
        stemmed_words = [stemmer.stem(word) for word in filtered_words]
        stemmed_words_sentence = nltk.Text(stemmed_words)
        stemmed_documents.append(stemmed_words_sentence)

        # Lemmatization
        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word.casefold()) for word in filtered_words]
        lemmatized_words_sentence = nltk.Text(lemmatized_words)
        lemmatized_documents.append(lemmatized_words_sentence)

