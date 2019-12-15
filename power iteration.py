# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 08:35:27 2019

@author: ANUBHAB JOARDAR
"""

#power iteration

import numpy as np

#eigen vector
A=np.array([[2,-12],[1,-5]])
x0=np.array([[1],[1]])

oval=np.linalg.eig(A)
print("eigen values determined are ",oval)

def pi(A,x):
    x1=np.dot(A,x)
    x2=abs((x1/np.min(abs(x1))))-abs((x/np.min(abs(x))))
    if abs(x2[0,0])>0.0001:
        pi(A,x1)
    fx=x1/np.min(abs(x1))
    return fx
    
evec=abs(pi(A,x0))
print("eigen vector is",evec)

#eigen value
tmp1=np.dot(A,evec)
tmp2=np.dot(np.transpose(evec),evec)
l=np.dot(np.transpose(tmp1),evec)/tmp2
print(tmp1)
print(tmp2)
print("eigen value is ", l)