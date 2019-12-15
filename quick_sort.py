# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 10:35:28 2019

@author: ANUBHAB JOARDAR
"""

#quick sort
a=[1,45,67,23,13,98,46]

def partition(x,low,up):
    pivot=x[up]
    i=low-1
    for j in range(low,up):
        if x[j]<pivot:
            i+=1
            x[i],x[j]=x[j],x[i]
    x[i+1],x[up]=x[up],x[i+1]
    return(i+1)
    
def quisort(x,start,end):
    if start<end:
        brk= partition(x,start,end)
        quisort(x,start,brk-1)
        quisort(x,brk+1,end)
        
quisort(a,0,len(a)-1)
print(a)
    