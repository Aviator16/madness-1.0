# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 17:01:28 2019

@author: ANUBHAB JOARDAR
"""

#regression
import random as rd
import numpy as np

oy= rd.sample(range(1000),100)
ox= rd.sample(range(1000),100)
y=rd.sample(oy,70)
x=rd.sample(ox,70)
ry=np.setdiff1d(oy,y)
rx=np.setdiff1d(ox,x)

r=np.corrcoef(x,y)
print("correlation is",r)
sy=sum(y)
sx=sum(x)
tmp1=np.multiply(x,y)
sxy=sum(tmp1)
tmp2=np.multiply(x,x)
sx2=sum(tmp2)
c1=(sxy-(sxy/100))/(sx2-((sx/100)**2))
print("c1 is",c1)
tmp3=np.multiply(c1,x)
sc1x=sum(tmp3)
c0=(sy-sc1x)/100
print("c0 is",c0)
sumdif=0
for i in range(30):
    ey=c0+c1*rx[i]
    print("estimated y value is",ey)
    diy=ry[i]-ey
    print("Difference is",diy)
    sumdif=sumdif+diy
avgdif=sumdif/30
print("Average difference between estimated value and original value is",avgdif)