import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
iris = pd.read_csv('D:/[Coding Ninjas] Machine Learning and Data Science/14. Project - Case Study (Part - I)/startup_funding.csv')
df = iris.copy()
df = df[df.CityLocation != '']
df['CityLocation'].replace("Delhi", "New Delhi", inplace = True)
df['CityLocation'].replace("bangalore", "Bangalore", inplace = True)
df['CityLocation'] = df.CityLocation.str.split('/').str[0]
df['CityLocation'] = df.CityLocation.str.replace(' ' , '')
#print(df['CityLocation'])
dict = {}
for i in df.CityLocation:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

# print(dict)
xaxis=[]
yaxis=[]

for i in dict.keys():
    if i!='nan' and i == 'Bangalore' or i == 'NewDelhi' or i == 'Noida' or i == 'Gurgaon' or i == 'Mumbai':
        xaxis.append(i)
        yaxis.append(dict[i])

for i in range(len(xaxis)):
    print(xaxis[i] , yaxis[i])

np_xaxis=np.array(xaxis)
np_yaxis=np.array(yaxis)
plt.bar(np_xaxis, np_yaxis, color='red')
plt.xlabel("City")
plt.xticks(rotation = 40)
plt.ylabel("Number Of Fundings")
plt.title("City vs Number Of Fundings")
plt.show()
