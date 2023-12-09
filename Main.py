import numpy as np
import pandas as pd
import csv
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

stemmed_documents = []
lemmatized_documents = []

query_sentences = []
stemmed_query_words = []
lemmatized_query_words = []

stop_words = set(stopwords.words("english"))
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

with open('dblp-v10.csv', newline='', encoding="utf8") as csvfile:
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

        filtered_words = []
        for word in words:
            if word.casefold() not in stop_words:
                filtered_words.append(word)

        # Stemming
        stemmed_words = [stemmer.stem(w) for w in filtered_words]
        stemmed_words_sentence = nltk.Text(stemmed_words)
        stemmed_documents.append(stemmed_words_sentence)

        # Lemmatization
        lemmatized_words = [lemmatizer.lemmatize(w.casefold()) for w in filtered_words]
        lemmatized_words_sentence = nltk.Text(lemmatized_words)
        lemmatized_documents.append(lemmatized_words_sentence)

with open('queries.txt', newline='') as f:
    for line in f:
        query_sentences.append(line.strip())

for query in query_sentences:
    query_words = nltk.word_tokenize(query)

    filtered_query_words = []
    for query_word in query_words:
        if query_word.casefold() not in stop_words:
            filtered_query_words.append(query_word)
    
    ############# Stemming ############# 
    stemmed_query_words = [stemmer.stem(w) for w in filtered_query_words]

    found_docs_stemmed = []
    for i in range(len(stemmed_documents)):
        match = False
        for stemmed_query_word in stemmed_query_words:
            if stemmed_query_word in stemmed_documents[i]:
                match = True
                break
        
        if match:
            found_docs_stemmed.append(i + 1)
    
    print("STEMMED => Query", query_words, "found in", len(found_docs_stemmed), "documents. ") #They are", found_docs_stemmed)
    
    ############# Lemmatization #############
    lemmatized_query_words = [lemmatizer.lemmatize(w.casefold()) for w in filtered_query_words]

    found_docs_lemmatized = []
    for i in range(len(lemmatized_documents)):
        match = False
        for lemmatized_query_word in lemmatized_query_words:
            if lemmatized_query_word in lemmatized_documents[i]:
                match = True
                break
        
        if match:
            found_docs_lemmatized.append(i + 1)
    
    print("LEMMATIZED => Query", query_words, "found in", len(found_docs_lemmatized), "documents. ") #They are", found_docs_lemmatized)

