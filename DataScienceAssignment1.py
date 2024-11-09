# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# DS - Class-3: Python Tutorial
#import needed libraries
import numpy as np
import pandas as pd
import os
import math
import matplotlib.pyplot as plt

# Data Creation
Z7 = np.zeros((7,7), dtype=int)

R55 = np.array([[2,5,7,9, 11],[7,8,9, 5,7],[1,5,7,4,5],[7,9,8,5, 6], [1,7,5,7,5]])
#----------------------------------------------------------
# Data Storage
dir_path = r"C:\Users\Meiga\Documents\DATA3001"
file_name = "R55.npy"
file_path = os.path.join(dir_path, file_name)
np.save(file_path, R55) 
#----------------------------------------------------------
# Data Extraction
E25 = R55[1,4] # element on the 1st row and 4th column
Row3 = R55[2,:] # the second row
Col3 = R55[:,2] # the 1st column
Sub1334 = R55[0:3,2:4] # section
#----------------------------------------------------------
# Data Modification
R55Mod = np.copy(R55)
R55Mod[0:3,2:4] = Z7[0:3,2:4]
#----------------------------------------------------------
# Searching through data
# using for loops
SE = 5
indexSE = np.zeros((49,2),dtype=int)#rows and cols indices in 1 & 2
count = 0
for row in range(6):
    for col in range(6):
        if (int(R55[row,col])==SE):
           indexSE[count,0] = row
           indexSE[count,1] = col
           count = count + 1
           
# using Boolean/Logical matrices and the where() function
R55Bool = R55==SE # this creates the boolean matrix by applying the comparison operators to the original array
R55SE = R55[R55Bool]#to obtain the SE, simply put boolean matix inside of original

#using the where() function in python to locate the indices
SELoc = np.where(R55Bool)
#----------------------------------------------------------
# Sorting Data
R55_SortR = np.sort(R55,axis=1) # sort by rows
R55_SortC = np.sort(R55,axis=0) # sort by columns
#----------------------------------------------------------
# Obtain Basic Statistics: 
R55median = np.median(R55)
R55minimum= np.min(R55[5,:])
R55maximum=np.max(R55[:,3])
R55std=np.std(Sub1334)

#----------------------------------------------------------
# Plotting Data: 
# X-points starting at 10, ending at 90, and incrementing by 0.3 
x = np.arange(0, 50, 0.2) 
# Cosine values of X-points 
y = np.sin(x) 
# Plot the cosine graph 
plt.plot(x, y);plt.xlabel('X');plt.ylabel('Y = sin(X)');plt.show()
#----------------------------------------------------------
# Creating a Function 
def add3Nos(L,W,H): 
   return L+W+H
# Test Case
a = 10; b = 2; c = 4
d = add3Nos(a,b,c)
print(d)
