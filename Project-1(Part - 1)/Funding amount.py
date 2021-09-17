import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
iris = pd.read_csv('D:/[Coding Ninjas] Machine Learning and Data Science/14. Project - Case Study (Part - I)/startup_funding.csv')
df = iris.copy()
df.drop(df.index[df.CityLocation.isnull()], inplace=True)
df.reset_index(inplace=True, drop=True)
x2 = []
df['AmountInUSD'] = df.AmountInUSD.str.replace(',','')
df['AmountInUSD'] = df['AmountInUSD'].fillna(0)
x1 = df['AmountInUSD']
np_amount=np.array(x1, dtype='int64')
df[df.CityLocation == 'bangalore'] = 'Bangalore'
df[df.CityLocation == 'Delhi'] = 'New Delhi'
df['CityLocation'] = df.CityLocation.str.split('/').str[0]
df['CityLocation'] = df.CityLocation.str.replace(' ' , '')
x2 = df['CityLocation']
dict = {}
for i in range(len(x2)):
    if x2[i] in dict:
        dict[x2[i]] += np_amount[i]
    else:
        dict[x2[i]] = np_amount[i]

xaxis=[]
yaxis=[]

for i in dict.keys():
        xaxis.append(i)
        yaxis.append(dict[i])

np_xaxis=np.array(xaxis)
np_yaxis=np.array(yaxis)
np_xaxis=np_xaxis[np.argsort(np_yaxis)]
np_yaxis=np.sort(np_yaxis)
np_xaxis=np_xaxis[len(np_xaxis)-1:len(np_xaxis)-1-10:-1]
np_yaxis=np_yaxis[len(np_yaxis)-1:len(np_yaxis)-1-10:-1]
# plt.pie(np_yaxis, labels=np_xaxis, autopct='%.2f%%')
plt.bar(np_xaxis, np_yaxis, color='red')
plt.show()
# df.drop(df.index[df.CityLocation.isnull()], inplace=True)
# df.reset_index(inplace=True, drop=True)
# df.loc[df['AmountInUSD'].isnull(), 'AmountInUSD']='0'
# df.loc[df.CityLocation=='bangalore','CityLocation']='Bangalore'
# df.loc[df.CityLocation=='Delhi', 'CityLocation']='New Delhi'
#
# city=[]
# amount=[]
# for i in df.CityLocation:
#     city.append(i)
# for i in df.AmountInUSD:
#     amount.append(i)
#
# for i in range(len(amount)):
#     amount[i]=''.join(amount[i].split(','))
#     city[i]=city[i].split('/')[0].strip()
# np_amount=np.array(amount, dtype='int64')
# np_city=np.array(city)
#
# dic=dict()
# for i in range(len(np_city)):
#     if np_city[i] in dic:
#         dic[np_city[i]]+=np_amount[i]
#     else:
#         dic[np_city[i]]=np_amount[i]
#
# print(dic)
# xaxis=list(dic.keys())
# yaxis=list(dic.values())
#
# np_xaxis=np.array(xaxis)
# np_yaxis=np.array(yaxis)
#
# np_xaxis=np_xaxis[np.argsort(np_yaxis)]
# np_yaxis=np.sort(np_yaxis)
#
# np_xaxis=np_xaxis[len(np_xaxis)-1:len(np_xaxis)-1-10:-1]
# np_yaxis=np_yaxis[len(np_yaxis)-1:len(np_yaxis)-1-10:-1]
#
# plt.subplots(figsize=(15, 10))
# plt.bar(np_xaxis, np_yaxis, color='red')
# plt.xticks(rotation=45, size=16)
# plt.yticks(size=16)
# plt.xlabel('City--->', size=16)
# plt.ylabel('Funding--->', size=16)
# plt.show()
#
# for i in range(len(np_xaxis)):
#     print(np_xaxis[i],'-->', format((np_yaxis[i]*100)/sum(np_yaxis), '.2f'), 'Percent')
