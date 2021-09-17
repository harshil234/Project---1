import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
iris = pd.read_csv('D:/[Coding Ninjas] Machine Learning and Data Science/14. Project - Case Study (Part - I)/startup_funding.csv')
df = iris.copy()
df.drop(df.index[df.InvestorsName.isnull()], inplace=True)
df.reset_index(inplace=True, drop=True)
df['InvestorsName'] = df['InvestorsName'].replace(['Undisclosed investors','Undisclosed investor','Undisclosed Investor','Undisclosed','Undisclosed Dubai based HNIs','Undisclosed Ex Mckinsey Directors and Partners','Undisclosed HNI investors','Undisclosed HNIs','Undisclosed US Based Investors','Undisclosed Investors Investors','Undisclosed Investorss','undisclosed investors','Undisclosed Investors HNIs'],'Undisclosed Investors')
# print(df['InvestorsName'].value_counts().to_string())
df = df[df.InvestorsName != 'Undisclosed Investors']
df['InvestorsName'] = df.InvestorsName.str.split(',').str[0]
# print(df['InvestorsName'].value_counts().to_string())
dict = {}
for i in df.InvestorsName:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

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
# plt.pie(np_yaxis, labels=np_xaxis, autopct='%.2f%%')
plt.bar(np_xaxis, np_yaxis, color='red')
plt.xlabel("Investors name")
# plt.xticks(rotation = 40)
plt.ylabel("Number Of Fundings")
plt.title("Investors vs Number Of Fundings")
plt.show()
