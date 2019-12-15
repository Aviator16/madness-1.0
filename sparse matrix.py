# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 17:13:32 2019

@author: curaj
"""

#sparse matrix
import numpy as np

x,y=input("Enter the number of rows and column of the matrix: ").split(" ")
rnum=int(x,10)
cnum=int(y,10)
mat=np.zeros((rnum,cnum),dtype=int)
nz=int(input("Enter number of non-zero elements: "),10)
vrow=[]
vcol=[]
for i in range(nz):
    a,b,c=input("Enter the row, column and value of the non zero element: ").split(" ")
    mat[(int(a,10))-1][(int(b,10))-1]=int(c,10)
    if a not in vrow:
        vrow.append(a)
    if b not in vcol:
        vcol.append(b)
print("Our original matrix is")
print(mat)
print("")
spmat=np.zeros((nz+1,3),dtype=int)
spmat[0][0]=len(vrow)
spmat[0][1]=len(vcol)
spmat[0][2]=nz
spr=1
spc=0
for i in range(rnum):
    for j in range(cnum):
        if mat[i][j]!=0:
            spmat[spr][spc]=i+1
            spc=spc+1
            spmat[spr][spc]=j+1
            spc=spc+1
            spmat[spr][spc]=mat[i][j]
            spr=spr+1
            spc=0
print("Required sparse matrix is:")
print(spmat)
            
    


