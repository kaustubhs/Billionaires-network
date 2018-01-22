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

G=zen.Graph()
f=open('output_new.csv')
csv_f=csv.reader(f)

row=[r for r in csv_f]
			
for i in range(0,len(row)):

    first=row[i][0]
    second=row[i][1]
    weight_1=row[i][2]

    if (float(weight_1)!=0):
        G.add_edge(first,second,weight=float(weight_1))
##
zen.io.gml.write(G,'Billion.gml')

d3 = d3js.D3jsRenderer(G, interactive=False, autolaunch=True)
d3.clear()
G=zen.io.gml.read('Billion.gml',directed=False)
d3.set_graph(G)
d3.update()


