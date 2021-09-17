import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
iris = pd.read_csv('D:/[Coding Ninjas] Machine Learning and Data Science/14. Project - Case Study (Part - I)/startup_funding.csv')
df = iris.copy()
df = df[df.CityLocation != '']
df[df.CityLocation == 'bangalore'] = 'Bangalore'
df[df.CityLocation == 'Delhi'] = 'New Delhi'
df['CityLocation'] = df.CityLocation.str.split('/').str[0]
df['CityLocation'] = df.CityLocation.str.replace(' ' , '')
#print(df['CityLocation'])
dict = {}
for i in df.CityLocation:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)
xaxis=[]
yaxis=[]

for i in dict.keys():
    if i!='nan' and dict[i] != 179:
        xaxis.append(i)
        yaxis.append(dict[i])

np_xaxis=np.array(xaxis)
np_yaxis=np.array(yaxis)
np_xaxis=np_xaxis[np.argsort(np_yaxis)]
np_yaxis=np.sort(np_yaxis)
np_xaxis=np_xaxis[len(np_xaxis)-1:len(np_xaxis)-1-10:-1]
np_yaxis=np_yaxis[len(np_yaxis)-1:len(np_yaxis)-1-10:-1]
plt.pie(np_yaxis, labels=np_xaxis, autopct='%.2f%%')
plt.show()
# with open('D:/[Coding Ninjas] Machine Learning and Data Science/14. Project - Case Study (Part - I)/startup_funding.csv', encoding='utf8') as file_obj:
#     file_data=csv.DictReader(file_obj, skipinitialspace=True)
#     city=[]
#     for row in file_data:
#         city.append(row['CityLocation'])
#     np_city=np.array(city)
#     np_city=np_city[np_city != '']
#
#     for i in range(len(np_city)):
#         if 'bangalore' in np_city[i]:
#             np_city[i]='Bangalore'
#         if np_city[i]=='Delhi':
#             np_city[i]='New Delhi'
#
#     for i in range(len(np_city)) :
#         np_city[i]=np_city[i].split('/')[0].strip()
#
#     dic=dict()
#     for i in np_city:
#         if i in dic.keys():
#             dic[i]+=1
#         else:
#             dic[i]=1
#
#     xaxis=[]
#     yaxis=[]
#
#     for i in dic.keys():
#         xaxis.append(i)
#         yaxis.append(dic[i])
#     np_xaxis=np.array(xaxis)
#     np_yaxis=np.array(yaxis)
#
#     np_xaxis=np_xaxis[np.argsort(np_yaxis)]
#     np_yaxis=np.sort(np_yaxis)
#     np_xaxis=np_xaxis[len(np_xaxis)-1:len(np_xaxis)-1-10:-1]
#     np_yaxis=np_yaxis[len(np_yaxis)-1:len(np_yaxis)-1-10:-1]
#
#     plt.pie(np_yaxis, labels=np_xaxis, autopct='%.2f%%')
#     plt.show()
#
#     for i in range(len(np_xaxis)):
#         print(np_xaxis[i], np_yaxis[i], 'Start-ups')
