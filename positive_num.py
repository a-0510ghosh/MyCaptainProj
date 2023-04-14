# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:18:29 2023

@author: g_sha
"""

l=eval(input("enter a list with positive and negative numbers"))
emp=[]
for i in l:
    if i>0:
        emp.append(i)
    else:
        continue
print(emp)