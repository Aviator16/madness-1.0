# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:35:11 2019

@author: ANUBHAB JOARDAR
"""

import numpy as np

A=np.array([[16,3],[7,-11]])
b=np.array([[11],[13]])
x=np.array([[1],[1]])

L=np.zeros((2,2),dtype=int)
U=np.zeros((2,2),dtype=int)
for i in range(2):
    for j in range(2):
        if(i>=j):
            L[i][j]=A[i][j]
        else:
            U[i][j]=A[i][j]
print(U)
print(L)

li=np.linalg.inv(L)
T=-(np.dot(li,U))
C=np.dot(li,b)
def gsm(T,x,C):
    x1=np.dot(T,x)+C
    if np.allclose(x1,x):
        print(x1)
        print(np.dot(A,x1))
    else:
        gsm(T,x1,C)
        
gsm(T,x,C)
