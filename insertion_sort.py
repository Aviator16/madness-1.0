# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 20:07:21 2019

@author: ANUBHAB JOARDAR
"""

#Insertion sort
a=[1,4,67,32,41,89,30,6,16]
def insersort(x):
    for i in range(1,len(x)):
        tmp=i
        for j in range(i-1,0,-1):
                if x[tmp]<x[j]:
                    x[j],x[tmp]=x[tmp],x[j]
                tmp=tmp-1
    print(x)

insersort(a)
            