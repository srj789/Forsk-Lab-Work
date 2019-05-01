'''
Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
'''
val=[]
for i in range(0,4):
    N=input("Enter a string")
    val.append(N)
    

import re
for i in range(0,4):
    result=re.match(r"[-+]?\d*\.+\d+",val[i])
    if result:
        print("True")
    else:
        print("False")
