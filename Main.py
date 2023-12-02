import numpy as np
import pandas as pd
import csv

with open('dblp-v10_sample.csv', newline='') as csvfile:
    myreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in myreader:
        print(', '.join(row))