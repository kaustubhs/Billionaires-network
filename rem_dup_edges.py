import zen
import numpy
import unicodedata
import sys
sys.path.append('../zend3js/')
import d3js
import csv
import progressbar
import numpy.linalg as la
import matplotlib.pyplot as plt
from scipy.linalg import solve


f=open('Dataset.csv')
csv_f=csv.reader(f)

row=[r for r in csv_f]
##print (len(row))

i=0
bar = progressbar.ProgressBar(maxval=len(row), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()

while i < len(row):
    bar.update(i+1)
    k=i+1
    while k< len(row):
        if(row[i][0]==row[k][1] and row[i][1]==row[k][0]):
                    del row[k]
                    k=k-1
        k=k+1
    i=i+1
bar.finish()

with open("output_new.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(row)
