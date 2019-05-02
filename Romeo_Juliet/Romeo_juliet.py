# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:38:38 2019

@author: Suraj  kumar
"""
list1=[]
file=open('C:/Users/Suraj  kumar/Desktop/Forsk_Lab/Romeo_Juliet/romeo.txt',"r",encoding="utf8")

count=dict()
for line in file:
    words = line.split()
    list1.append(words)
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
print("\nList of Words: ")
print("----------------------------------------------")
print(list1)
print("\nWord counts are: ")
print("----------------------------------------------")
print(count)


import re
file2=open('C:/Users/Suraj  kumar/Desktop/Forsk_Lab/Romeo_Juliet/romeo2.txt',"r",encoding="utf8")
data=file2.read()
result=re.sub('[^A-Za-z\s]','',data)
print(result)
dict_=dict()
for line in result.split():
        if line not in dict_:
            dict_[line]=1
        else:
            dict_[line]+=1

print("\nWord counts :")
print(dict_)
            