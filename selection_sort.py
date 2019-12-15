# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 19:48:39 2019

@author: ANUBHAB JOARDAR
"""

#selection sort
a=[1,3,45,16,39,4,55,29]
print("array is ", a)
def selsort(x):
    for i in range(0,len(x)):
        tmp=i
        for j in range(i,len(x)):
            if x[j]<x[tmp]:
                tmp=j
        if tmp!=i:
            x[i],x[tmp]=x[tmp],x[i]
        
    print("sorted array is ",x)
    
selsort(a)