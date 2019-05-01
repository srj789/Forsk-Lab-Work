"""

Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
    yogendra_54@forsk.com
  Output:
    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]

"""
import re
val=[]
for i in range(0,3):
    N=input("Enter %d  Email address :"%(i))
    val.append(N)
list1=[]    
for i in range(0,3):
    result=re.match(r"^[A-Za-z0-9_\-]+@[A-Za-z0-9]+\.([a-zA-Z]){2,4}$",val[i])
    if result:
        list1.append(val[i])
list1.sort()
print(list1)