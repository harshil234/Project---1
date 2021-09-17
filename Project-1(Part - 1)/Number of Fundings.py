import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
iris = pd.read_csv('D:/[Coding Ninjas] Machine Learning and Data Science/14. Project - Case Study (Part - I)/startup_funding.csv')
df = iris.copy()
df['year'] = df['Date'].str.split('/').apply(lambda x: x[-1])
df[df['AmountInUSD'].isnull()] = 0
dict = {}
for row in df.year:
    if row in dict:
        dict[row] += 1
    else:
        dict[row] = 0
#print(dict)
j = 0
Year = []
value = []
for i in dict:
    #print(dict[i] , i)
    if i!=0 and i!='05.2015' and i!='04.2015' and i!='01.2015':
        Year.append(i)
        value.append(dict[i])

#print(Year)
#print(value)
plt.scatter(Year , value)
plt.plot(Year , value)
plt.show()
# with open('D:/[Coding Ninjas] Machine Learning and Data Science/14. Project - Case Study (Part - I)/startup_funding.csv', encoding='utf8') as file_obj:
#     file_data=csv.DictReader(file_obj, skipinitialspace=True)
#     year=[]
#     for row in file_data:
#         year.append(row['Date'][len(row['Date'])-4:])
#     np_year=np.array(year, dtype='int')
#     dic=dict()
#     for i in np_year:
#         if i in dic.keys():
#             dic[i]+=1
#         else:
#             dic[i]=1
# print(row['Date'][len(row['Date'])-4:])
# print(dic)
