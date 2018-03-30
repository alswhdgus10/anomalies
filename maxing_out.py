# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 00:04:20 2018

@author: 삼성컴퓨터
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import scipy

os.chdir('C:\\Users\\mjh\\Documents\\maxing_out')
data=pd.read_excel('data.xlsx', index_col='TIME')
data.index=pd.DatetimeIndex(data.index)

data_max=data.resample('M').max()
data_max_t=data_max.T
data_max_t_a=data_max_t.sort_values(['2012-01-31'], ascending=[True])
# print(data_max_t_a.index.values)
df=pd.DataFrame()
b=[]
for i in list(data_max_t.columns.values):
    data_max_t_a=data_max_t.sort_values([i], ascending=[True])
    b.append(data_max_t_a.index.values)

# print(b)
f_buffer=[]
s_buffer=[]
t_buffer=[]
for i in range(len(b)):
    first=b[i][:20]
    second=b[i][20:40]
    third=b[i][40:]
    f_buffer.append(first)
    s_buffer.append(second)
    t_buffer.append(third)
    
f_r=[]   
for j in range(len(list(data_max_t.columns.values))-1):
    f_buffer_r = []
    for i in range(len(f_buffer[0])):
        a = data_max_t[data_max_t.index.str.startswith(f_buffer[j][i])].iloc[0]
        f_buffer_r.append(a[j+1])
    f_r.append(f_buffer_r)


s_r=[]   
for j in range(len(list(data_max_t.columns.values))-1):
    s_buffer_r = []
    for i in range(len(s_buffer[0])):
        a = data_max_t[data_max_t.index.str.startswith(s_buffer[j][i])].iloc[0]
        s_buffer_r.append(a[j+1])
    s_r.append(s_buffer_r)
    
t_r=[]   
for j in range(len(list(data_max_t.columns.values))-1):
    t_buffer_r = []
    for i in range(len(t_buffer[0])):
        a = data_max_t[data_max_t.index.str.startswith(t_buffer[j][i])].iloc[0]
        t_buffer_r.append(a[j+1])
    t_r.append(t_buffer_r)
    
f_mean=[]

for i in f_r:
    listSum = sum(i)
    listLength = len(i)
    f_mean.append(listSum / listLength)

s_mean=[]
for i in s_r:
    listSum = sum(i)
    listLength = len(i)
    s_mean.append(listSum / listLength)

t_mean=[]
for i in t_r:
    listSum = sum(i)
    listLength = len(i)
    t_mean.append(listSum / listLength)

f_mean = pd.DataFrame(f_mean)
s_mean = pd.DataFrame(s_mean)
t_mean = pd.DataFrame(t_mean)

pf=pd.concat([f_mean,s_mean,t_mean], axis=1)
pf.index=data_max.index[1:]

pf.to_csv('maxing_out_result.csv')
