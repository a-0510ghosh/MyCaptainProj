# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n=int(input("enter number the number of terms wanted in the series"))
n1,n2=0,1
c=0
if  n<= 0:
    print("enter a valid positive number")
elif n==1:
    print("fibonacci series upto",n,":")
    print(n1)
else:
    print("fibonacci series")
    while c<n:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        c+=1
