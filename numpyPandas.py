# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:09:39 2019

@author: RufinoS
"""

import numpy as np
import pandas as pd

arr = np.arange(1,20,2,dtype="float64")


arr.ndim
arr2 =  np.asarray([[1,2,3],[4,5,6]])
listZeros = np.zeros((3,4),dtype="int32")

listZeros

np.linspace(1,4, num = 8)
#returns 8 numbers evenly spaced within range

rarr = np.random.random((3,4))

np.max(rarr, axis=1)

new_rarr = np.reshape(rarr, (12,))

#slicing
rarr = np.random.random((4,5))

rarr[:,:]
rarr[0:3, :]
rarr[2:3, :]
rarr[1:3, 1:3]
rarr[[0,3], :]
rarr[:,[0,3]]
rarr[:-1,:]

x = pd.Series([1,2,3,4,5])

x+100
x**2
larger_than_2 = x > 2
larger_than_2.any()
larger_than_2.all()

def f(x):
    if x%2 == 0:
        return x**2
    else:
        return x**3
    
x.apply(f)

y = x.copy()
y[0] = 100
y
 
#dataframes
data = [1,2,3,4,5,6,7,8,9]
df = pd.DataFrame(data, columns=["x"])

dataseries = df["x"]

df["x_plus_2"] = df["x"] + 2

df = df.drop("x_plus_2", 1)

df.describe

