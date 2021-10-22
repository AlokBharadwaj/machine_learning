#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 23:05:07 2021

@author: alok
"""
from tqdm import tqdm
import pandas_datareader as web
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew

mean = {}
std = {}
sk = {}
kurt = {}

for year in tqdm(range(2015,2022)):
    for month in range(1,12):
      
        if year == 2021 and month >=10:
            break
        start = dt.datetime(year,month,1)
        end = dt.datetime(year,month+1,1)
        index="BTC-USD"
        
        stock = web.DataReader(index,'yahoo',start,end)
        
        stock_close = stock['Close']

        stock_change = np.gradient(stock_close)
        mean[year+month/12]=stock_change.mean()
        std[year+month/12]=stock_change.std()
        sk[year+month/12]=skew(stock_change)
        kurt[year+month/12]=kurtosis(stock_change)

    
    
plt.figure(1)
plt.plot(list(mean.keys()),list(mean.values()),'bo-')
plt.ylabel("Average daily change {}".format(index))
plt.figure(2)
plt.plot(list(std.keys()), list(std.values()),'bo-')
plt.ylabel("{} hype".format(index))

plt.figure(3)
plt.plot(list(sk.keys()),list(sk.values()),'bo-')
plt.ylabel("{} monthly skew index ".format(index))

plt.figure(4)
plt.plot(list(kurt.keys()),list(kurt.values()),'bo-')
plt.ylabel("{} monthly kurtosis index ".format(index))


import seaborn as sns
import pandas as pd

df = pd.DataFrame(data=[list(mean.values()), list(std.values()), list(mean.keys())], index=['Avg_daily_change','Hype','Date']).T

plt.figure(5)
sns.relplot(data=df,x='Avg_daily_change',y='Hype',size='Date', hue='Date', palette="rainbow", hue_norm=(2017,2022))

def plot_month(year,month):
      start = dt.datetime(year,month,1)
      end = dt.datetime(year,month+1,1)
        
      stock = web.DataReader(index,'yahoo',start,end)
        
      stock_close = stock['Close']
      stock['Close'].plot(marker='o')

      stock_change = np.gradient(stock_close)
      #plt.hist(stock_change,bins=31)