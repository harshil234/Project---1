import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
iris = pd.read_csv('D:/[Coding Ninjas] Machine Learning and Data Science/14. Project - Case Study (Part - I)/startup_funding.csv')
df = iris.copy()
df.drop(df.index[df.InvestmentType.isnull()], inplace=True)
df.reset_index(inplace=True, drop=True)
df['AmountInUSD'] = df.AmountInUSD.str.replace(',','')
df['AmountInUSD'] = df['AmountInUSD'].fillna(0)
x1 = df['AmountInUSD']
np_amount=np.array(x1, dtype='int64')
df[df.InvestmentType == 'SeedFunding'] = 'Seed Funding'
df[df.InvestmentType == 'PrivateEquity'] = 'Private Equity'
df[df.InvestmentType == 'Crowd funding'] = 'Crowd Funding'
# print(df['InvestmentType'].unique())
x2 = df['InvestmentType']
dict = {}
for i in range(len(x2)):
    if x2[i] in dict:
        dict[x2[i]] += np_amount[i]
    else:
        dict[x2[i]] = np_amount[i]

print(dict)
xaxis=[]
yaxis=[]

for i in dict.keys():
        xaxis.append(i)
        yaxis.append(dict[i])

plt.pie(yaxis, labels=xaxis, autopct='%.2f%%')
plt.show()
