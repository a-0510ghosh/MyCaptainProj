# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 07:20:39 2023

@author: g_sha
"""
import operator
def most_frequent(string):
    f_dict={}
    for l in string:
         if l in f_dict:
             f_dict[l] +=1
         
         else:
             f_dict[l]=1
             
    sorted_dict = sorted(f_dict.items(), key=operator.itemgetter(1), reverse=True)

    for letter, freq in sorted_dict:
        print(f"{letter}: {freq}")
        
print (most_frequent("mississippi"))