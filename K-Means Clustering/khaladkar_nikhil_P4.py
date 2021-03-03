# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 00:33:13 2020

@author: nikkh

Name: Nikhil Khaladkar
CuId: C23185416
"""
import numpy as np
import matplotlib.pyplot as plt
import math

#print uncluster data
def print_unclustered_data(dataSet,centroid_data):
    
    for data in dataSet:
        data_plot=plt.scatter(data[0],data[1],color="purple",marker="o",label="data")
    
    
    for centroid in centroid_data: 
        centroid_plot=plt.scatter(centroid[0], centroid[1], color="red",marker="*",label="centroids")    
    plt.title("Unclustered Data")
   
    plt.legend((data_plot,centroid_plot),('Data Points','Centroids'),loc="upper right")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()
    
    plt.close()
    return
      
#calculate the eculedian distance.  
def calculate_distance(centroid,point):
    
    term_1=pow(centroid[0]-point[0],2)
    term_2=pow(centroid[1]-point[1],2)
    
    
    return math.sqrt(term_1+term_2)


# calculate the cost function   
def calculate_cost(cluster,centroid):
    cost=0
    for point in cluster:
        cost+=pow(calculate_distance(point,centroid),2)
        
    return cost    
        
# cluster the data into K=2 Clusters and print the data. 
def cluster_data(dataSet,centroid_data):
    
    centroid_1=centroid_data[0]
    centroid_2=centroid_data[1]
    old_cost=0
    clustering_cost=0
    c1_cluster=[]
    c2_cluster=[]
     
    while True:
        old_cost=clustering_cost
        
        c1_cluster=[]
        c2_cluster=[]
      
        for point in dataSet:
            dist_from_c1=calculate_distance(centroid_1,point)
            dist_from_c2=calculate_distance(centroid_2,point)
            if dist_from_c1>dist_from_c2:
                c2_cluster.append(point)
            else:
                c1_cluster.append(point)
        centroid_1=np.mean(c1_cluster,axis=0)
        centroid_2=np.mean(c2_cluster,axis=0)
        c1_cost=calculate_cost(c1_cluster,centroid_1)
        c2_cost=calculate_cost(c2_cluster,centroid_2)
        clustering_cost=(1/len(dataSet)*(c1_cost+c2_cost))
        if(clustering_cost==old_cost):
            break;
       
    
  
    
    for c1_point in c1_cluster:
        c1_data_plot=plt.scatter(c1_point[0], c1_point[1],color="red",marker="o",label="Final Cluster 1 Data")
    
    for c2_point in c2_cluster:
        c2_data_plot=plt.scatter(c2_point[0], c2_point[1],color="green",marker="v",label="Final Cluster 2 Data")
        
        
    centroid_c1_plot=plt.scatter(centroid_1[0], centroid_1[1],color="black",marker="o",label="Final Cluster 1 Centroid")
    centroid_c2_plot=plt.scatter(centroid_2[0], centroid_2[1],color="black",marker="v",label="Final Cluster 2 Centroid")    
    plt.title("Clustered Data")
    plt.legend((c1_data_plot,c2_data_plot,centroid_c1_plot,centroid_c2_plot),('C1 Points','C2 Points','C1 Centroid','C2 Centroid'),loc='upper right')
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.show()
   
    plt.close()
    print('-------------------------------------------------')
    print('Centroid 1 Co-ordinates')
    print('-------------------------------------------------')
    print(centroid_1)
    print('-------------------------------------------------')
    print('Centroid 2 Co-ordinates')
    print('-------------------------------------------------')
    print(centroid_2)
    print('-------------------------------------------------')
    print('Overall Error')
    print('-------------------------------------------------')
    print("Error is\t"+str(clustering_cost))
    return        

#main function
if  __name__=="__main__":
    
    data_file=input("Enter the name of the data file:\t")
    
    file_handle=open(data_file,'r')
    
    data_dim_line=file_handle.readline()
    
    number_of_points=int(data_dim_line.split('\t')[0])
    number_of_columns=int(data_dim_line.split('\t')[1])

    dataSet=[]
    #read the data
    for row in range(number_of_points):
        line=file_handle.readline()
        linedata=line.split('\t')
       
        for column in range(number_of_columns):
           
            linedata[column]=float(linedata[column])
        
        dataSet.append(linedata)
        
    
    #print the data
    #print(dataSet)
    file_handle.close()
    centroid_file=input("Enter the centroid file name:\t")
    centroid_file_handle=open(centroid_file,'r')
    
    number_of_centroids=int(centroid_file_handle.readline().strip())
    
    centroid_data=[]
    for centroids in range(number_of_centroids):
        line=centroid_file_handle.readline()
        
        centroid_points=line.split('\t')
        for centroid_column in range(2):
            centroid_points[centroid_column]=float(centroid_points[centroid_column])
        centroid_data.append(centroid_points)
    
    print('-------------------------------------------------')
    print('Initial Centroid Data')
    print('-------------------------------------------------')
    print(centroid_data)
    
    
    print_unclustered_data(dataSet,centroid_data)
    
    cluster_data(dataSet,centroid_data)
            
            
        
    


            
            
            
    