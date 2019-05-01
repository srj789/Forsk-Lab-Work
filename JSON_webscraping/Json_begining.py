# -*- coding: utf-8 -*-
"""
Created on Wed May  1 12:26:26 2019

@author: Suraj  kumar
"""

"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
import json
faculty={}
faculty['suraj']={
        'First Name':'Suraj',
        'Last Name':'Kumar',
        'Photo':'www.dsfssmmfk.com',
        'Department':'Cse',
        'Research Areas':['machine learning','Deep learning'],
        'Contact details':{'mob':'9087654321','email':'er.srj789@gmail.com'}
        }
faculty['aman']={
        'First Name':'aman',
        'Last Name':'Kumar',
        'Photo':'www.dsfsfk.com',
        'Department':'mechnaical',
        'Research Areas':['mototrs','animation'],
        'Contact details':{'mob':'2143567654','email':'srtyf.9@gmail.com'}
        }
jsonfile=json.dumps(faculty)
jsonfile