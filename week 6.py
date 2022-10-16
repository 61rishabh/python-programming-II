# -*- coding: utf-8 -*-
"""Week5-6_Pandas_Numpy_Matplotlib.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/133DLRbWYhhev4eivwmDCo3AftiOgo2yl
"""

import numpy as np
a = np.array([2,3,4,5])

type(a)

np.array([[1,2,3],[3,4,5],[3,6,7]])

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')

df

df.plot(kind = 'area',alpha =0.1,stacked = False)

df.plot.scatter(x='sepal_length',y = 'sepal_width')

df.plot.scatter(x='sepal_length',y = 'petal_length', c='sepal_length')

df.plot.scatter(x='sepal_width',y = 'petal_width')

df.plot.scatter(x='sepal_length',y='petal_length', c='sepal_width',s=df['sepal_length']*10)

df.plot.hexbin(x='sepal_length',y='petal_length', gridsize=10,cmap="viridis")

from mpl_toolkits import mplot3d

x = np.linspace(-1,6,30)

y=np.linspace(-1,6,30)

y

z = x+y

def sin_fun(x,y):
    return np.sin(np.sqrt(x**2+y**2))

z = sin_fun(x,y)

ax = plt.axes(projection = '3d')
ax.plot3D(x,y,z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel("z")

ax = plt.axes(projection = '3d')
ax.plot3D(df['sepal_length'],df['petal_length'],df['petal_width'])
ax.set_xlabel('sepal_length')
ax.set_ylabel('petal_length')
ax.set_zlabel("sepal_width")

df.plot(figsize=(30,15))

df.iloc[50:70].plot(kind = 'bar',figsize=(15,7.5))

df.iloc[50:70].plot(kind = 'barh',figsize=(15,8))

df.plot(kind='hist', figsize=(18,9))

df

df['petal_length'].plot(kind='hist',figsize=(10,10))

df.hist(figsize=(25,10), color='#50DBB4', alpha=0.6)

import cufflinks as cf
cf.go_offline()

df

df.iplot()

df.iplot(x='sepal_length', y='sepal_width', kind='scatter', mode = 'markers')

df.iplot(x='sepal_length', y='sepal_width', size = 'sepal_length',kind='bubble')

df.iplot(x='sepal_length', y='sepal_width', z = 'petal_length',size = 'sepal_length',kind='bubble3d')

df1 = sns.load_dataset('tips')

df1

df1.iplot(x='total_bill',y='tip', kind = 'scatter', mode ='markers')

sns.relplot(x='total_bill', y='tip', data = df1, hue = 'size')

df1

df1['smoker'].value_counts()

sns.relplot(x='total_bill', y='tip', data = df1, col = 'sex')

sns.relplot(x='total_bill', y='tip', data = df1, col = 'time')

sns.relplot(x='sepal_length', y='sepal_width', data = df, col = 'species')

sns.relplot(x='total_bill', y='tip', data=df1, col='day')

sns.catplot(x='day', y='total_bill', data=df1)

sns.pairplot(df1)

df.scatter_matrix()

df1 = sns.load_dataset('tips')

sns.jointplot(x=df1.total_bill, y=df1.tip)

sns.pairplot(df1)

sns.regplot(x=df1.total_bill, y=df1.tip)
sns.set(rc={'figure.figsize':(20,10)})

df1