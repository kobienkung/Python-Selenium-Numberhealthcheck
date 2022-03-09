import csv
import pandas as pd
import numpy as np
import glob

path = r'C:\Users\kobienkung\OneDrive - KMITL\Python Selenium Numberhealthcheck'
files = glob.glob(path + '/*.csv')

li = []
for file in files:
    df = pd.read_csv(file, index_col=None, header=0)
    li.append(df)

df = pd.concat(li, axis=0, ignore_index=True)
df['aSum'] = df.iloc[:,5:11].sum(axis=1)
df[df['aSum'] == 5]


