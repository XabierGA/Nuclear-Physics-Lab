# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 10:53:24 2018

@author: xabia
"""

import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np
import seaborn as sns

sns.set()

data1 = pd.read_excel('nuclearwoa.xlsx')
data2 = pd.read_excel('nuclear_la.xlsx')

arr1 = data1.values
arr2 = data2.values

volt1 = []
volt2 = []
time1 = []
time2 = [] 

steps = np.arange(2,len(arr1) , 1)

for i in (steps): 
    
    time1.append(float(arr1[i][0].split(',')[0]))
    volt1.append(float(arr1[i][0].split(',')[1]))
    time2.append(float(arr2[i][0].split(',')[0]))
    volt2.append(float(arr2[i][0].split(',')[1]))
    
    
plt.figure(num=None, figsize=(9, 7), dpi=100, facecolor='w', edgecolor='k', )
plt.plot(time1,volt1 , label = 'Without Amplification')
#plt.plot(time2,volt2 , 'r-', label='Amplification')
plt.xlabel('Time ($\mu s$)')
plt.ylabel('Voltage (mV)')
plt.title('Oscilloscope Measurements')
plt.legend(prop={'size':13})
plt.grid(True)

plt.savefig('withoutamplif.pdf')



