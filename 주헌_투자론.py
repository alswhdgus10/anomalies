# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 03:46:04 2018

@author: Jooheon
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import scipy

os.chdir("C:/Users/Jooheon/Desktop")

def get_data(file_name = 'dataa.xlsx'):
    xls = pd.ExcelFile(file_name)
    data = xls.parse(0, header = 8, index_col = 0)
    data = data.reindex(index = data.index[5:])
    data.index = pd.to_datetime(data.index, format='%Y-%m-%d')

    return data
data = get_data()
data = (data.dropna(axis=1)).iloc[:,:425]


def get_cd(file_name = 'dataa.xlsx'):
    xls = pd.ExcelFile(file_name)
    data = xls.parse(1, header = 8, index_col = 0)
    data = data.reindex(index = data.index[5:])
    data.index = pd.to_datetime(data.index, format='%Y-%m-%d')

    return data




def get_KOSPI(file_name = 'dataa.xlsx'):
    xls = pd.ExcelFile(file_name)
    data = xls.parse(2, header = 8, index_col = 0)
    data = data.reindex(index = data.index[5:])
    data.index = pd.to_datetime(data.index, format='%Y-%m-%d')

    return data



data_max=data.resample('M').max()
data_max_t=data_max.T
cd = pd.DataFrame(get_cd()['Economy']/12)
cd.columns = [0]
cd.index = data_max.index[1:]

def get_mret(file_name = 'dataa.xlsx'):
    xls = pd.ExcelFile(file_name)
    data = xls.parse(3, header = 8, index_col = 0)
    data = data.reindex(index = data.index[5:])
    data.index = pd.to_datetime(data.index, format='%Y-%m-%d')
    return data
mret = get_mret()
mret.index = data_max.index
mret = (mret.dropna(axis=1)).iloc[:,:425]
mret_t = mret.T

Kospi = pd.DataFrame((get_KOSPI())['I.004'])
Kospi.columns = [0]
Kospi.index=data_max.index[1:]
Kospi = Kospi - cd
Kospi.columns = ['KOSPI']



# print(data_max_t_a.index.values)
df=pd.DataFrame()
b=[]
for i in list(data_max_t.columns.values):
    data_max_t_a=data_max_t.sort_values([i], ascending=[True]) #확인해보잠
    b.append(data_max_t_a.index.values)

# print(b)
f_buffer=[]
s_buffer=[]
t_buffer=[]
q_buffer=[]
w_buffer=[]
for i in range(len(b)):
    first=b[i][:85]
    second=b[i][85:170]
    third=b[i][170:255]
    fourth=b[i][255:340]
    fifth=b[i][340:]
    f_buffer.append(first)
    s_buffer.append(second)
    t_buffer.append(third)
    q_buffer.append(fourth)
    w_buffer.append(fifth)
    
f_r=[]   
for j in range(len(list(mret_t.columns.values))-1):
    f_buffer_r = []
    for i in range(len(f_buffer[0])):
        a = mret_t[mret_t.index.str.startswith(f_buffer[j][i])].iloc[0]
        f_buffer_r.append(a[j+1])
    f_r.append(f_buffer_r)


s_r=[]   
for j in range(len(list(mret_t.columns.values))-1):
    s_buffer_r = []
    for i in range(len(s_buffer[0])):
        a = mret_t[mret_t.index.str.startswith(s_buffer[j][i])].iloc[0]
        s_buffer_r.append(a[j+1])
    s_r.append(s_buffer_r)
    
t_r=[]   
for j in range(len(list(mret_t.columns.values))-1):
    t_buffer_r = []
    for i in range(len(t_buffer[0])):
        a = mret_t[mret_t.index.str.startswith(t_buffer[j][i])].iloc[0]
        t_buffer_r.append(a[j+1])
    t_r.append(t_buffer_r)

q_r=[]
for j in range(len(list(mret_t.columns.values))-1):
    q_buffer_r = []
    for i in range(len(q_buffer[0])):
        a = mret_t[mret_t.index.str.startswith(q_buffer[j][i])].iloc[0]
        q_buffer_r.append(a[j+1])
    q_r.append(q_buffer_r)
    
w_r=[]
for j in range(len(list(mret_t.columns.values))-1):
    w_buffer_r = []
    for i in range(len(w_buffer[0])):
        a = mret_t[mret_t.index.str.startswith(w_buffer[j][i])].iloc[0]
        w_buffer_r.append(a[j+1])
    w_r.append(w_buffer_r)
    
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

q_mean=[]
for i in q_r:
    listSum = sum(i)
    listLength = len(i)
    q_mean.append(listSum / listLength)
    
w_mean=[]
for i in w_r:
    listSum = sum(i)
    listLength = len(i)
    w_mean.append(listSum / listLength)


f_mean = pd.DataFrame(f_mean)
f_mean.index = data_max.index[1:]
f_mean = f_mean - cd


s_mean = pd.DataFrame(s_mean) 
s_mean.index = data_max.index[1:]
s_mean = s_mean - cd
s_mean.columns = ['2']

t_mean = pd.DataFrame(t_mean)
t_mean.index = data_max.index[1:]
t_mean = t_mean - cd 
t_mean.columns = ['3']

q_mean = pd.DataFrame(q_mean)
q_mean.index = data_max.index[1:]
q_mean = q_mean - cd 
q_mean.columns = ['4']

w_mean = pd.DataFrame(w_mean)
w_mean.index = data_max.index[1:]
w_mean = f_mean - cd


f_w = f_mean - w_mean
f_w.columns = ['low-high']
f_mean.columns = ['MAX 1 (low)']
w_mean.columns = ['MIN 5 (high)']

pf=pd.concat([f_mean,s_mean,t_mean,q_mean,w_mean,f_w,Kospi], axis=1)
pf.index=data_max.index[1:]


#f_mean.to_csv('f_mean.csv')
#s_mean.to_csv('s_mean.csv')
#t_mean.to_csv('t_mean.csv')
pf.to_csv('pf.csv')
