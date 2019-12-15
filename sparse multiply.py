# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:41:34 2019

@author: ANUBHAB JOARDAR
"""

#sparse multiplication

import numpy as np

m1=np.array([[3,2,3],[1,1,1],[2,2,3],[3,2,2]])
m2=np.array([[3,3,3],[1,2,5],[2,3,1],[3,1,4]])
print("First sparse matrix is ")
print(m1)
print("")
print("Second sparse matrix is ")
print(m2)
print("")

def sparseprod(mat1,mat2):
    prods={}
    for i in range(1,len(mat1[:,1])):
        tmp=[]
        for j in range(1,len(mat2[:,1])):
            if mat1[i,1]==mat2[j,0]:
                tmp.append(mat1[i,2]*mat2[j,2])
                prods.update({10*mat1[i,0]+mat2[j,1]:tmp})
    
    pos=[k for k in prods]
    pmat=np.zeros((len(pos)+1,3),dtype=int)
    rl=[]
    cl=[]
    for r in range(1,len(pos)+1):
        pmat[r,0]=pos[r-1]//10
        pmat[r,1]=pos[r-1]%10
        pmat[r,2]=sum(prods[pos[r-1]])
        
        if pmat[r,0] not in rl:
            rl.append(pmat[r,0])
        if pmat[r,1] not in cl:
            cl.append(pmat[r,1])
    pmat[0,0]=len(rl)
    pmat[0,1]=len(cl)
    pmat[0,2]=len(pos)
        
    print("The product of the two matrices in Sparse matrix form is")
    print(pmat)

sparseprod(m1,m2)

#another example
'''m3=np.array([[2,2,3],[1,1,1],[2,1,-1],[2,3,3]])
m4=np.array([[2,2,2],[1,1,7],[3,3,1]])
sparseprod(m3,m4)'''