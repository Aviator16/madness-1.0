# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 21:11:48 2019

@author: ANUBHAB JOARDAR
"""

#merge sort
a=[1,45,3,2,78,56,14,23,16]

def mergsort(x):
    if len(x)>1:    
        m=len(x)//2
        L=x[:m]
        R=x[m:]
        #print(L,R)
        mergsort(L)
        mergsort(R)
    
        i=j=k=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                x[k]=L[i]
                i=i+1
            else:
                x[k]=R[j]
                j=j+1
            k=k+1
           # print("abc",i,j)
        #print(i,j)    
        while i<len(L):
            x[k]=L[i]
            i+=1
            k+=1
        while j<len(R):
            x[k]=R[j]
            j+=1
            k+=1
        #print("def",i,j)
    
mergsort(a)
print(a)