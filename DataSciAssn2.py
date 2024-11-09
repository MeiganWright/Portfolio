# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 17:25:18 2023

@author: Meiga
"""

import numpy as np
import pandas as pd
import os
import math
import matplotlib.pyplot as plt

dir_path =r"C:\Users\Meiga\Downloads"
file_name="train.csv"
file_path= os.path.join(dir_path, file_name)
if os.path.exists (dir_path):
    df=pd.read_csv(file_path)
    print('File was created.')
else: 
    print("No directory found.")
    
#Q1
Age_Data=df.loc[:,'Age']
Age_Mean=Age_Data.mean(skipna=True)
Age_Clean=Age_Data.fillna(Age_Mean)

#Q2
#Establishing the filter requirements
Fare_Data=df.loc[:,'Fare']
Fare_Low=18
Fare_High=40
Fare_Search = (Fare_Data>Fare_Low)&(Fare_Data<Fare_High)


#//Getting all True Values and placing them in a series
Filter = Fare_Search.index[Fare_Search == True]
#Listing individuals that paid between 18 and 40
ListofP=df.loc[Filter]
#Only Including Name and Class of those individuals
FinalList=ListofP[['Name', 'Pclass']]


#Q3
Survived_Data = df.loc[:,'Survived']
Guest_Nos = len(Survived_Data)
Surv_Nos = sum(Survived_Data)



Sex_Data=df.loc[:,'Sex']
MaleL=Sex_Data=='male' 
   
Class_Data=df.loc[:,'Pclass']
class2L= Class_Data==2

Age_Low=25
Age_High=45
MidAgeM=(Age_Clean>Age_Low)&(Age_Clean<Age_High)

GC= np.multiply(MaleL,class2L)
GCA=np.multiply(GC,MidAgeM)

Prob_GCA=sum(GCA)/Surv_Nos


