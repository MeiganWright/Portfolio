# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:49:20 2023

@author: Meiga

Meant to calculate and Plot the Data for further data co-relation
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

#Read Date column as DateTime format, Extract only First week of July
df['Date']=pd.to_datetime(df['Date'])
df=df.loc[(df['Date']>= '2017-07-01') & (df['Date'] <= '2017-07-08')]

#Calculate average cyclists per hour for every hour, Calculate percentage difference per hour
MedianTPH = df.groupby('Time')['Total'].median()
CyclistsPH= df.groupby(['Day', 'Time'])['Total'].median()
PHD = 100*(CyclistsPH-MedianTPH)/MedianTPH

# Average cyclists per hour for every day of the First week of July
for Day in df['Day'].unique():
    DayData = df.loc[df['Day']==Day]
    MedianT = DayData.groupby('Time')['Total'].median()
    plt.plot(MedianT.index, MedianT, label=Day)

#Plot Graph 1
plt.title('Total Cyclist vs Hour')
plt.xlabel('Hours')
plt.ylabel('Average Cyclist Total')
plt.show()

#Plot Graph 2
plt.plot(PHD.index.get_level_values('Time'), PHD.values, 'o')
plt.title('Percentage of Total Cyclists vs Average Cyclist by the hour')
plt.axhline(y=0, color='b', linestyle='--')
plt.xlabel('Hours')
plt.ylabel('PHD- Percentage Hour Difference')
plt.show()