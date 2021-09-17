import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
iris = pd.read_csv('D:/[Coding Ninjas] Machine Learning and Data Science/14. Project - Case Study (Part - I)/startup_funding.csv')
df = iris.copy()
df['StartupName'] = df.StartupName.str.replace('Flipkart.com','Flipkart')
df['StartupName'] = df.StartupName.str.replace('Ola Cabs','Ola')
df['StartupName'] = df.StartupName.str.replace('Olacabs','Ola')
df['StartupName'] = df.StartupName.str.replace('Oyo Rooms','Oyo')
df['StartupName'] = df.StartupName.str.replace('OyoRooms','Oyo')
df['StartupName'] = df.StartupName.str.replace('Oyorooms','Oyo')
df['StartupName'] = df.StartupName.str.replace('Paytm Marketplace','Paytm')
# print(df[df.StartupName.str.contains('Ola')])
df['AmountInUSD'] = df.AmountInUSD.str.replace(',','')
df['AmountInUSD'] = df['AmountInUSD'].fillna(0)
x1 = df['AmountInUSD']
np_amount=np.array(x1, dtype='int64')
x2 = df['StartupName']
# print(x1)
dict = {}
for i in range(len(x2)):
    if x2[i] in dict:
        dict[x2[i]] += np_amount[i]
    else:
        dict[x2[i]] = np_amount[i]

# print(dict)
xaxis=[]
yaxis=[]

for i in dict.keys():
        xaxis.append(i)
        yaxis.append(dict[i])

np_xaxis=np.array(xaxis)
np_yaxis=np.array(yaxis)
np_xaxis=np_xaxis[np.argsort(np_yaxis)]
np_yaxis=np.sort(np_yaxis)
np_xaxis=np_xaxis[len(np_xaxis)-1:len(np_xaxis)-1-5:-1]
np_yaxis=np_yaxis[len(np_yaxis)-1:len(np_yaxis)-1-5:-1]
plt.pie(np_yaxis, labels=np_xaxis, autopct='%.2f%%')
# plt.bar(np_xaxis, np_yaxis, color='red')
plt.show()
