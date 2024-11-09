# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 16:47:47 2023

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
    
Date = df['DateTime']
Date_Str = Date.to_string()
Month = Date.str.slice(0,2)
Day = Date.str.slice(3,5)
Year = Date.str.slice(6,10)   

Month=pd.to_numeric(Month)
Day=pd.to_numeric(Day)
Year=pd.to_numeric(Year)

Year_2016= Year==2016
Year_2017= Year==2017 
Month_July= Month==7

July2016=(Year_2016)&(Month_July)
July2017=(Year_2017)&(Month_July)

cyT = df['Total']
cyT_July2016 = cyT[July2016]
no_days_July2016=round(len(cyT_July2016)/96)
cyT_July2016_Avg=sum(cyT_July2016)/no_days_July2016

cyT_July2017=cyT[July2017]
no_days_July2017=round(len(cyT_July2017)/96)
cyT_July2017_Avg=sum(cyT_July2017)/no_days_July2017

#-------------------------------------------------------------------------

dir_path_W = r"C:\Users\Meiga\Downloads"
file_name_W = "Boston weather_clean.csv"
file_path_W = os.path.join(dir_path_W, file_name_W)

if os.path.exists (dir_path_W):
    df_W = pd.read_csv(file_path_W)
    print('File was created.')
else:
    print("Directory doesn\'t exist.")
    
Year_W= df_W['Year']
Month_W=df_W['Month']

Year2016_W= Year_W==2016  
Year2017_W= Year_W==2017  
Month_JulyW= Month_W==7

July2016_W= (Year2016_W)&(Month_JulyW) 
July2017_W=(Year2016_W)&(Month_JulyW)


#---------Humidity--------------#
#Humidity Average for 2016
Humid= df_W['Avg Humidity (%)']
Humid=pd.to_numeric(Humid)
HumidJuly_2016= Humid[July2016_W]
HumidJuly2016_Avg=HumidJuly_2016.mean()
#Humidity Average for 2017
HumidJuly_2017=Humid[July2017_W]
HumidJuly2017_Avg=HumidJuly_2017.mean()

#High Humidity
HumidHigh_2016= HumidJuly_2016 > HumidJuly2016_Avg
HumidHigh_2017= HumidJuly_2017 > HumidJuly2017_Avg

#Days
Days_W=df_W['Day']
DaysJuly2016_W= Days_W[July2016_W]
DaysHighHumidity2016=DaysJuly2016_W[HumidHigh_2016]

DaysJuly2017_W= Days_W[July2017_W]
DaysHighHumidity2017=DaysJuly2017_W[HumidHigh_2017]


#----------Wind-----------#
#Wind Average for 2016
Wind = df_W['Avg Wind (mph)']
Wind=pd.to_numeric(Wind)
Wind2016=Wind[July2016_W]
Wind2016_Avg=Wind2016.mean()
#Wind Average for 2017
Wind2017=Wind[July2017_W]
Wind2017_Avg=Wind2017.mean()

#High Wind
WindHigh_2016= Wind2016 > Wind2016_Avg
WindHigh_2017= Wind2017 > Wind2017_Avg

#Days
DaysHighWind2016=DaysJuly2016_W[WindHigh_2016]
DaysHighWind2017=DaysJuly2017_W[WindHigh_2017]


#-----Precipitation-----#
#Precip Average for 2016
Precip=df_W['Precip (in)']
Precip=pd.to_numeric(Precip)
Precip2016=Precip[July2016_W]
Precip2016_Avg=Precip2016.mean()

#Precip Average for 2017
Precip2017=Precip[July2017_W]
Precip2017_Avg=Precip2017.mean()

#High Precipitation
PrecipHigh_2016= Precip2016 > Precip2016_Avg
PrecipHigh_2017= Precip2017 > Precip2017_Avg

#Days
DaysHighPrecip2016= DaysJuly2016_W[PrecipHigh_2016]
DaysHighPrecip2017= DaysJuly2017_W[PrecipHigh_2017]



#------------Number of Days for each condition----------#
TotalDaysHumid2016=len(DaysHighHumidity2016)
TotalDaysHumid2017=len(DaysHighHumidity2017)

TotalDaysWind2016=len(DaysHighWind2016)
TotalDaysWind2017=len(DaysHighWind2017)

TotalDaysPrecip2016=len(DaysHighPrecip2016)
TotalDaysPrecip2017=len(DaysHighPrecip2017)

#----------Cyclists on target dates-------#
CyDays_2016=Day[July2016]
CyDays_2017=Day[July2017]

#Initializing lists 
cyT_HH2016=list()
cyT_HH2017=list()        
cyT_HW2016=list() 
cyT_HW2017=list() 
cyT_HP2016=list() 
cyT_HP2017=list() 

#High Humidity
i=0
for i in range(0, TotalDaysHumid2016):
    Day_W=DaysHighHumidity2016.iloc[i]
    Day_C= CyDays_2016==Day_W
    Day_C_CyT=cyT_July2016[Day_C]
    cyT_HH2016.append(Day_C_CyT.sum())

for i in range(0, TotalDaysHumid2017):
    Day_W2=DaysHighHumidity2017.iloc[i]
    Day_C2= CyDays_2017==Day_W2
    Day_C_CyT2=cyT_July2017[Day_C2]
    cyT_HH2017.append(Day_C_CyT2.sum())
    
#High Wind
for i in range(0, TotalDaysWind2016):
    Day_W3=DaysHighWind2016.iloc[i]
    Day_C3= CyDays_2016==Day_W3
    Day_C_CyT3=cyT_July2016[Day_C3]
    cyT_HW2016.append(Day_C_CyT3.sum())
    
for i in range(0, TotalDaysWind2017):
    Day_W4=DaysHighWind2017.iloc[i]
    Day_C4= CyDays_2017==Day_W4
    Day_C_CyT4=cyT_July2017[Day_C4]
    cyT_HW2017.append(Day_C_CyT4.sum())

#High Precipitation
for i in range(0, TotalDaysPrecip2016):
    Day_W5=DaysHighPrecip2016.iloc[i]
    Day_C5= CyDays_2016==Day_W5
    Day_C_CyT5=cyT_July2016[Day_C5]
    cyT_HP2016.append(Day_C_CyT5.sum())

for i in range(0, TotalDaysPrecip2017):
    Day_W6=DaysHighPrecip2017.iloc[i]
    Day_C6= CyDays_2017==Day_W5
    Day_C_CyT6=cyT_July2017[Day_C6]
    cyT_HP2017.append(Day_C_CyT6.sum())
 
    
 #------------Plotting Graphs------------#
plt.barh(DaysHighHumidity2016 ,cyT_HH2016, color=['Blue','Red'])
plt.xlabel('Cyclists')
plt.ylabel('Days in Month')
plt.title("Total Cyclists vs High Humidity July 2016")
plt.show()

plt.barh(DaysHighHumidity2017 ,cyT_HH2017, color=['Green','Magenta'])
plt.xlabel('Cyclists')
plt.ylabel('Days in Month')
plt.title("Total Cyclists vs High Humidity July 2017")
plt.show()

plt.barh(DaysHighWind2016 ,cyT_HW2016, color=['Blue','Red'])
plt.xlabel('Cyclists')
plt.ylabel('Days in Month')
plt.title("Total Cyclists vs High Wind July 2016")
plt.show()

plt.barh(DaysHighWind2017 ,cyT_HW2017, color=['Green','Magenta'])
plt.xlabel('Cyclists')
plt.ylabel('Days in Month')
plt.title("Total Cyclists vs High Wind July 2017")
plt.show()

plt.barh(DaysHighPrecip2016 ,cyT_HP2016, color=['Blue','Red'])
plt.xlabel('Cyclists')
plt.ylabel('Days in Month')
plt.title("Total Cyclists vs High Precipitation July 2016")
plt.show()

plt.barh(DaysHighPrecip2017 ,cyT_HP2017, color=['Green','Magenta'])
plt.xlabel('Cyclists')
plt.ylabel('Days in Month')
plt.title("Total Cyclists vs High Precipitation July 2017")
plt.show()