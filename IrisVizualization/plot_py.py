# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:58:30 2020

@author: nikhilkhaladkar
"""

import numpy as np
import matplotlib.pyplot as plt
#declare the rows variable to count the number of entries in the data.
rows=0

fileHandle= open("IrisData.txt","r")

line= fileHandle.readline()
#count number of entries
while line:
    
    line=fileHandle.readline()
    rows=rows+1

fileHandle.close()

#create np array of rows=150 (found from the previous step) and columns=5
data = np.zeros([int(rows),5])

#read the data and store the data into the array above. For setosa set value 1 , for versicolor value 2 and virginica value 3.
newfileHandle= open("IrisData.txt","r")

#iterating till the secondlast line since the last line is taken as blank line. Map Setosa to 1, Versicolor to 2 and virginica to 3
for index in range(rows-1):
    line=newfileHandle.readline()
    lines=line.strip()
    lineArray=lines.split("\t")
    for j in range(4):
        data[index,j] = float(lineArray[j])
    if lineArray[4] == 'setosa':
        data[index,4] = 1
    if lineArray[4] == 'versicolor':
        data[index,4] = 2
    if lineArray[4] == 'virginica':
        data[index,4] = 3
#close the file handle
newfileHandle.close()

#based on the class select the respective marker to plot the data.
for k in range(rows):
    if data[k,4] == 1:
        Setosa= plt.scatter(data[k,0],data[k,2],color="red",marker="o",label="Setosa")

    elif data[k,4] == 2:
        Versicolor= scatter=plt.scatter(data[k,0],data[k,2],color="green",marker="v",label="Versicolor")
      
    elif data[k,4] == 3:
        Virginica= scatter=plt.scatter(data[k,0],data[k,2],color="blue",marker="^",label="Virginica")
    
#plot the data using matplotlib object
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Iris Data Sepal Length vs Petal Length")
plt.legend((Setosa,Versicolor,Virginica),('Setosa','Versicolor','Virginica'),loc="lower right")
plt.savefig("my_plot.png",bbox_inches="tight")
plt.show()

    
        

        