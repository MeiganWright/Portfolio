# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:43:02 2023

@author: Meiga
"""

import numpy as np
import pandas as pd
import os
import math
import matplotlib.pyplot as plt
from datetime import datetime

dir_path = r"C:\Users\Meiga\Downloads"
file_name = "Eco-Totem_Broadway_Bicycle_Count_20231111.csv"
file_path = os.path.join(dir_path, file_name)

if os.path.exists (dir_path):
    df=pd.read_csv(file_path)
    print('File was created.')
else: 
    print('File does not exist.')

#Converting Date column to Datetime format
df['Date']=pd.to_datetime(df['Date'])

#Calculate Median T for each month in 2017
MedianT = df.loc[df['Date'].dt.year==2017, ['Date', 'Total']].groupby(df['Date'].dt.month).median()

#Graph 1
plt.plot(MedianT.index, MedianT['Total'])
plt.title('Average Monthly Cyclists for 2017')
plt.xlabel('Months by Number')
plt.ylabel('Average Cyclists')
plt.show()

#calculate needed coffee per month
CoffeePM=(MedianT['Total']/4) *0.05

#Graph 2
plt.plot(CoffeePM.index, CoffeePM)
plt.title('Coffee Bags to Purchase by Month')
plt.xlabel('Months')
plt.ylabel('Coffee To Purchase (Approx.)')
plt.show()