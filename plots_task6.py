# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 22:28:22 2018

@author: xabia
"""

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
import seaborn as sns
import pandas as pd
sns.set()

def lin_func(x,a,b):
        return a*x+b

inten_cu = [2701.8,1764.5,1358.2,1065.7,819.3,688.6,536.1]
sinten_cu = [5.3,4.2,3.7,3.3,2.9,2.7,2.3]

thickness_cu = [0.00,0.50,1.00,1.50,2.00,2.50,3.10]
sthick_cu = [0.10,0.14,0.17,0.20,0.22,0.24 , 0.26]

lninten_cu = [3.4317,3.2466,3.1329,3.0276,2.9134,2.8380,2.7292]
slninten_cu = [0.0019,0.0024,0.0027,0.0031,0.0035,0.0039,0.0044]

coeff_cu , var_cu = curve_fit(lin_func , thickness_cu ,lninten_cu ,sigma = slninten_cu)


#plt.figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k', )
#plt.errorbar(thickness_cu , inten_cu, yerr = sinten_cu , xerr = sthick_cu,fmt='mo',label='Experimental Values', ms = 8)
#plt.xlabel('Thickness (cm)')
#plt.ylabel('Intensity $(counts/s)$')
#plt.title('Intensity as a function of the thickness of the copper')
#plt.legend(prop={'size':13})
#plt.grid(True)
#
#plt.savefig('cu_exponential.pdf')


#tt = np.linspace(0,3.1, 100000)
#plotnew = lin_func(tt, coeff_cu[0] , coeff_cu[1])
#plt.errorbar(thickness_cu , lninten_cu , yerr = slninten_cu , xerr = sthick_cu , fmt='mo',label='Experimental Values', ms = 8)
#plt.plot(tt, plotnew , 'b-' , label = 'Linear Fit')
#plt.xlabel('Thickness of the material (cm)')
#plt.ylabel('ln(I)')
#plt.title('Logarithm of the intensity as a function of the thickness of the copper')
#plt.legend(prop={'size':13})
#plt.grid(True)
#
#plt.savefig('cu_fit.pdf')

dataframe_al = pd.read_excel('task6_al.xlsx')

data_al = dataframe_al.values

inten_al = data_al[:,5]
sinten_al = data_al[:,6]

thickness_al = data_al[:,1]
sthick_al = data_al[:,2]

aux = [2588.44,2282.89,2059.54,1676.12,1390,1124.93,1058.9,914]

lninten_al = [np.log(dels) for dels in aux]
slninten_al = data_al[:,8]

coeff_al , var_al = curve_fit(lin_func , thickness_al ,lninten_al ,sigma = slninten_al)


#plt.figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k', )
#plt.errorbar(thickness_al , inten_al, yerr = sinten_al , xerr = sthick_al,fmt='mo',label='Experimental Values', ms = 8)
#plt.xlabel('Thickness (cm)')
#plt.ylabel('Intensity $(counts/s)$')
#plt.title('Intensity as a function of the thickness of the aluminum')
#plt.legend(prop={'size':13})
#plt.grid(True)
#
#plt.savefig('al_exponential.pdf')


#tt_al = np.linspace(0,max(thickness_al), 100000)
#plotnew_al = lin_func(tt_al, coeff_al[0] , coeff_al[1])
#plt.errorbar(thickness_al , lninten_al , yerr = slninten_al , xerr = sthick_al , fmt='mo',label='Experimental Values', ms = 8)
#plt.plot(tt_al, plotnew_al , 'b-' , label = 'Linear Fit')
#plt.xlabel('Thickness of the material (cm)')
#plt.ylabel('ln(I)')
#plt.title('Logarithm of the intensity as a function of the thickness of the aluminum')
#plt.legend(prop={'size':13})
#plt.grid(True)
#
#plt.savefig('al_fit.pdf')

dataframe_pb = pd.read_excel('task6_pb.xlsx')

data_pb = dataframe_pb.values

inten_pb = data_pb[:,4]
sinten_pb = data_pb[:,5]

thickness_pb = data_pb[:,0]
sthick_pb = data_pb[:,1]

lninten_pb = data_pb[:,6]
slninten_pb = data_pb[:,7]

coeff_pb , var_pb = curve_fit(lin_func , thickness_pb ,lninten_pb,sigma = slninten_pb )


plt.figure(num=None, figsize=(10, 8), dpi=100, facecolor='w', edgecolor='k', )
#plt.errorbar(thickness_pb , inten_pb, yerr = sinten_pb , xerr = sthick_pb,fmt='mo',label='Experimental Values', ms = 8)
#plt.xlabel('Thickness (cm)')
#plt.ylabel('Intensity $(counts/s)$')
#plt.title('Intensity as a function of the thickness of the lead')
#plt.legend(prop={'size':13})
#plt.grid(True)
#
#plt.savefig('pb_exponential.pdf')


tt_pb = np.linspace(0,max(thickness_pb), 100000)
plotnew_pb = lin_func(tt_pb, coeff_pb[0] , coeff_pb[1])
plt.errorbar(thickness_pb , lninten_pb , yerr = slninten_pb , xerr = sthick_pb , fmt='mo',label='Experimental Values', ms = 8)
plt.plot(tt_pb, plotnew_pb , 'b-' , label = 'Linear Fit')
plt.xlabel('Thickness of the material (cm)')
plt.ylabel('ln(I)')
plt.title('Logarithm of the intensity as a function of the thickness of the lead')
plt.legend(prop={'size':13})
plt.grid(True)

plt.savefig('pb_fit.pdf')

