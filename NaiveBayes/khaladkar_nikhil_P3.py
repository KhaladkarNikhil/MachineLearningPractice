# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 00:02:29 2020

@author: nikkh
Name: Nikhil Khaladkar
CUId:C23185416
"""
from math import*


'''function for cleaning the text and removing punctions and special symbols from the text''' 
def cleanText(line):
    line=line.lower()
    #remove trailing spaces.
    line=line.strip()
    for letters in line:
        if letters in """~[]!.,"--@;':#%^&*()+/?=""":
            line=line.replace(letters," ")
        
    
    return line
'''Calculate how many times a word in the vocab occurs in spam and ham headers'''
def countWords(words,is_spam,counted):
    
    for word in words:
        if word in counted:
            if is_spam==1:
                counted[word][1]=counted[word][1]+1
            else:
                counted[word][0]=counted[word][0]+1
        else:
            if is_spam==1:
                counted[word]=[0,1]
            else:
                counted[word]=[1,0]
    return counted
'''Calculate the percentage of the words in vocab that appeared in spams and hams'''
def calc_percent_for_words(k,counted,spams,hams):
    
    
    for word in counted:
        counted[word][1]=(k+ counted[word][1])/(2*k+spams)
        counted[word][0]=(k+ counted[word][0])/(2*k+hams)
    
    return counted

'''Predict the test headers to be spam or ham'''
def predict(vocab,test_words,probability_spam,probability_ham):

        spam_header=0
        ham_header=0
        for word in vocab:
            if word in test_words:
                spam_header=spam_header+log(vocab[word][1])
                ham_header=ham_header+log(vocab[word][0])
            else:
                spam_header=spam_header+log(1-vocab[word][1])
                ham_header=ham_header+log(1-vocab[word][0])

        
        total_spam_prob=exp(spam_header)
        total_ham_prob=exp(ham_header)
        
        probability_ham=log(total_ham_prob)+log(probability_ham)
        probability_spam =log(total_spam_prob)+log(probability_spam)
        
        bayes_theorem_exp=exp(probability_ham-probability_spam)
        
        final_probability=1/(1+bayes_theorem_exp)
        
        #print(final_probability)
        if final_probability>=0.5:
            return 1
        else:
            return 0
            
        return
'''Print the vocab table.'''
def printVocab(vocab):
    print("Word\tHamProb\tHamProb")
    for word in vocab:
        print(word+'\t'+str(vocab[word][0])+'\t'+str(vocab[word][1]))        

'''Print the F1 score of the Naive Bayes Model''' 
def printF1Score(y_test,y_predict):
    false_positive=0
    false_negative=0
    true_negative=0
    true_positive=0
    for i in range(len(y_test)):
        if y_test[i]==0 and y_predict[i]==0:
            true_negative=true_negative+1
        elif y_test[i]==1 and y_predict[i]==1:
            true_positive=true_positive+1
        elif y_test[i]==0 and y_predict[i]==1:
            false_positive=false_positive+1
        elif y_test[i]==1 and y_predict[i]==0:
            false_negative=false_negative+1
    print("----------------------\n")  
    print("FP:\t"+str(false_positive))
    print("FN:\t"+str(false_negative))
    print("TP:\t"+str(true_positive))
    print("TN:\t"+str(true_negative))
    print("----------------------\n")        
    accuracy=(true_positive+true_negative)/(true_positive+true_negative+false_negative+false_positive)
    print("Accuracy:\t"+str(accuracy))        
    print("----------------------\n")       
    precision=(true_positive)/(true_positive+false_positive)
    print("Precision:\t"+str(precision))
    print("----------------------\n")
    recall=(true_positive)/(true_positive+false_negative)
    print("Recall:\t"+str(recall))
    print("----------------------\n")
    f_1_score=2*(precision*recall)/(precision+recall)
    print("F1 Score:\t"+str(f_1_score))
    print("----------------------\n")
    return             
  
if  __name__=="__main__":
    
    train_file_name=input("Please enter the name of the trainng file " )
    train_file_name_handle=open(train_file_name,'r',encoding='utf8')
    stop_words_file=input("Please enter the name of the stop words file " )
    stop_words_file_handle=open(stop_words_file,'r')
    
    line=train_file_name_handle.readline()
    #intialize a dictionary for how many words in spam and ham.
    counted=dict()
    #spam count
    spam=0
    #ham count
    ham=0
    
    stop_words=[]
    
    stop_words_line=stop_words_file_handle.readline()
    while stop_words_line !="":
        stop_words.append(stop_words_line[:1])
        stop_words_line=stop_words_file_handle.readline()
    while line !="":
        
        is_spam=int(line[:1])
        if(is_spam == 1):
            spam=spam+1
        else:
            ham=ham+1
        line=cleanText(line[1:])
        words=line.split()
        words=set(words)
        words=words.difference(stop_words)
        counted=countWords(words,is_spam,counted)
        line = train_file_name_handle.readline()
    #print(counted)
    vocab=(calc_percent_for_words(1,counted,spam,ham))
    #printVocab(vocab)
  
    #print(spam)
    #print(ham)
    #close the file handlers for train file and stop words file.
    train_file_name_handle.close()
    stop_words_file_handle.close()
    probability_spam=spam/(spam+ham)
    probability_ham=ham/(spam+ham)
    test_file_name=input("Please enter the name of the test file\t")
    test_file_handler=open(test_file_name,'r',encoding='utf8')
    test_line=test_file_handler.readline()
    test_spam_class=[]
    predict_spam_class=[]
    
    test_spams=0
    test_hams=0
    while test_line!="":
        test_spam_class.append(int(test_line[:1]))
        if (int(test_line[:1]))==0:
            test_hams=test_hams+1
        else:
            test_spams=test_spams+1
            
        test_line=cleanText(test_line[1:])
        test_words=test_line.split()
        test_words=set(test_words)
        predicted_class=predict(vocab,test_words,probability_spam,probability_ham)
        predict_spam_class.append(predicted_class)
        test_line=test_file_handler.readline()
    
    
    print("Number of Spams in Test File\t"+str(test_spams))
    print("Number of Hams in Test File\t"+str(test_hams))
    printF1Score(test_spam_class,predict_spam_class)
        
        
    
