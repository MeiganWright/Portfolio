# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 19:32:00 2023

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


df['Date'] = pd.to_datetime(df['Date'])
df['Season'] = df['Date'].dt.month.apply(lambda x: 'Winter' if x in [12, 1,
2] else 'Spring' if x in [3, 4, 5] else 'Summer' if x in [6, 7, 8] else
'Fall')


Seasons = ['Spring', 'Summer', 'Fall', 'Winter']
Days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
'Sunday']

#Saving Average count OF Cyclists for each day for later use
AverageCount = {season: {day: 0 for day in Days} for season in Seasons}

#Calculate staff needed per day with Average cyclist count
for season in Seasons:
    for day in Days: 
        d_data = df[(df['Season'] == season) & (df['Day'] == day)]
        d_data['Total'] = d_data['Total'].fillna(0)
        AverageCount[season][day] = np.median(d_data["Total"])



#Calculate staff needed
staff_needed = {season: {day: 1 + int(count / 40) for day, count in Season_counts.items()} for Season, Season_counts in AverageCount.items()}


# Plot the data for each season
fig, axs = plt.subplots(nrows=len(Seasons), figsize=(10,20))
for i, Season in enumerate(Seasons):
    axs[i].bar(range(len(Days)), list(staff_needed[season].values()))
    axs[i].set_xticks(range(len(Days)))
    axs[i].set_xticklabels(Days)
    axs[i].set_ylabel('Staff Needed')
    axs[i].set_title(Season)
plt.tight_layout()
plt.show()