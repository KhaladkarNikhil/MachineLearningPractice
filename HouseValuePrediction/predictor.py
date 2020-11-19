# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:36:30 2020

@author: nikkh
C23185416
"""
import numpy as np

#function to calculate J value.
def calculateJ(m,X,w,y):
    #create an array of 1 so that the 
    m_ones=np.ones((m,1))
    numerator_J=np.dot(m_ones.T,np.power(np.dot(X,w)-y,2))  
    J=numerator_J/(2*m)
    return J
#function to calculate adjusted R-square
def calculateAdjustedRSquare(J,y,m,n):
    m_ones=np.ones((m,1))
    y_mean=np.mean(y)
    y_mean_square=(y-y_mean)*(y-y_mean)
    denominator=np.dot(m_ones.T,y_mean_square)/(2*m)
    print(denominator)
    r_square=1-(J/denominator)
    adjusted_r_square = (1-(((1-r_square)*(m-1))/(m-n-1)))
    return adjusted_r_square
    
  
     
#input filename for the train file
filename=input("Enter the training filename ")

#load the from the training set into an numpy array 
training_data_file=open(filename,'r')
training_data_shape_line=training_data_file.readline()

#get the data_entries and data_features
training_data_entries=int(training_data_shape_line.split('\t')[0])
training_data_features=int(training_data_shape_line.split('\t')[1])
#close the file handle
training_data_file.close()

#create an array for training_data
training_data=np.zeros((training_data_entries,training_data_features+1))
training_data=np.loadtxt(filename,skiprows=1,delimiter='\t')

#create a independent feature array by adding an x0=1 as the first feature 
X=np.ones((training_data_entries,training_data_features+1))
X[:,1:training_data_features+1]=np.copy(training_data[:,0:training_data_features])
#create y which is the dependent varaiable array
y=np.ones((training_data_entries,1))
y[:,0]=np.copy(training_data[:,training_data_features])


#lets apply the normal equation formula.

first_term=np.linalg.pinv(np.dot(X.T,X))
second_term=np.dot(X.T,y)

#calculate weight vector for the training set
weights=np.dot(first_term,second_term)

#print the weights
print('Weights Training Set:')
for i in range(weights.shape[0]):
    print('w_'+str(i)+':\t'+str(weights[i]))
train_J=calculateJ(training_data_entries,X,weights,y)
print('Final J for Training Set :')
print(train_J)

#input the filename for val/test set.
test_data_set_filename=input("Enter the filename for val/test dataset: ")


test_data_file=open(test_data_set_filename,'r')
#read the shape for the test/val file
test_data_shape_line=test_data_file.readline()
test_data_set_entries=int(test_data_shape_line.split('\t')[0])
test_data_set_features=int(test_data_shape_line.split('\t')[1])
test_data_file.close()
#load the test/val data.
test_data=np.ones((test_data_set_entries,test_data_set_features+1))
test_data=np.loadtxt(test_data_set_filename,skiprows=1,delimiter='\t')
#create the dependent features and independent feature array.
test_data_matrix=np.ones((test_data_set_entries,test_data_set_features+1))
test_data_matrix[:,1:test_data_set_features+1]=np.copy(test_data[:,0:test_data_set_features])
test_dependent_var=np.ones((test_data_set_entries,1))
test_dependent_var[:,0]=np.copy(test_data[:,test_data_set_features])
#calculate the J function
test_J=calculateJ(test_data_set_entries,test_data_matrix,weights,test_dependent_var)
#calculate the adjusted R-square value
adjusted_r_square=calculateAdjustedRSquare(test_J,test_dependent_var,test_data_set_entries,test_data_set_features)
print("Final J for the test/val set: ")
print(test_J)
print("Adjusted R square for the test/val set: ")
print(adjusted_r_square)
