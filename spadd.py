# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 01:51:49 2019

@author: ANUBHAB JOARDAR
"""
import numpy as np

mat1=np.array([[3,4,4],[1,4,12],[3,3,5],[4,1,15],[4,2,12]])
mat2=np.array([[3,4,4],[2,4,23],[3,3,9],[4,1,20],[4,2,25]])
print("First sparse matrix is ")
print(mat1)
print("")
print("Second sparse matrix is ")
print(mat2)
print("")


def sparseadd(mat1,mat2):
    adm=np.zeros((1,3),dtype=int)
    j=0
    for i in range(1,max(len(mat1[:,1]),len(mat2[:,1]))):
        mat3=np.zeros((1,3),dtype=int)
        if mat1[i][0]==mat2[i][0]:
            if mat1[i][1]==mat2[i][1]:
                mat3[0][0]=mat1[i][0]
                mat3[0][1]=mat1[i][1]
                mat3[0][2]=mat1[i][2]+mat2[i][2]
                adm=np.append(adm,mat3)
                j=j+1
        else:
            adm=np.append(adm,mat1[i][:])
            j=j+1
            adm=np.append(adm,mat2[i][:])
            j=j+1
        
    rl=[]
    rn=0
    cl=[]
    cn=0
    adm=adm.reshape(j+1,3)
    for i in range(1,j+1):
        if adm[i][0] not in rl:
            rl.append(adm[i][0])
            rn=rn+1
        if adm[i][1] not in cl:
                cl.append(adm[i][1])
                cn=cn+1
        
    adm[0][0]=rn
    adm[0][1]=cn
    adm[0][2]=j
            
    print("Addition of both sparse matrices is ")
    print(adm)
        
sparseadd(mat1,mat2)