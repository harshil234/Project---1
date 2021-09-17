import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv
import operator
iris = pd.read_csv('D:/[Coding Ninjas] Machine Learning and Data Science/14. Project - Case Study (Part - I)/startup_funding.csv')
df = iris.copy()
# df.dropna(subset=['InvestmentType', 'StartupName' ,'InvestorsName'],inplace=True)
# df['InvestmentType'].replace('SeedFunding','Seed Funding',inplace=True)
# df['InvestmentType'].replace('PrivateEquity','Private Equity',inplace=True)
# df['InvestmentType'].replace('Crowd funding','Crowd Funding',inplace=True)
# df['StartupName'].replace('Flipkart.com','Flipkart',inplace=True)
# df['StartupName'].replace('Ola Cabs','Ola',inplace=True)
# df['StartupName'].replace('Olacabs','Ola',inplace=True)
# df['StartupName'].replace('Oyo Rooms','Oyo',inplace=True)
# df['StartupName'].replace('Oyorooms','Oyo',inplace=True)
# df['StartupName'].replace('OyoRooms','Oyo',inplace=True)
# df['StartupName'].replace('OYO Rooms','Oyo',inplace=True)
# df['StartupName'].replace('Paytm Marketplace','Paytm',inplace=True)
# df['InvestorsName'] = df['InvestorsName'].replace(['Undisclosed investors','Undisclosed investor','Undisclosed Investor','Undisclosed','Undisclosed Dubai based HNIs','Undisclosed Ex Mckinsey Directors and Partners','Undisclosed HNI investors','Undisclosed HNIs','Undisclosed US Based Investors','Undisclosed Investors Investors','Undisclosed Investorss','undisclosed investors','Undisclosed Investors HNIs'],'Undisclosed Investors')
# df = df[df.InvestorsName != 'Undisclosed Investors']
# df['InvestorsName'] = df.InvestorsName.str.split(',').str[0]
# df = df[(df['InvestmentType'] == "Crowd funding") | (df['InvestmentType'] == "Seed Funding")]
# df = df['InvestorsName']
# # print(len(startup))
# dict = {}
# for i in df:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
#
# # print(dict)
df.dropna(subset=['InvestorsName','StartupName','InvestmentType'],inplace=True)
df['InvestmentType'].replace('PrivateEquity','Private Equity',inplace=True)
df['InvestmentType'].replace('SeedFunding','Seed Funding',inplace=True)
df['InvestmentType'].replace('Crowd funding','Crowd Funding',inplace=True)
df['InvestorsName'].replace('Undisclosed investors','Undisclosed Investors',inplace=True)
df['StartupName'].replace('Flipkart.com','Flipkart',inplace=True)
df['StartupName'].replace('Ola Cabs','Ola',inplace=True)
df['StartupName'].replace('Olacabs','Ola',inplace=True)
df['StartupName'].replace('Ola Cabs','Ola',inplace=True)
df['StartupName'].replace('Olacabs','Ola',inplace=True)
df['StartupName'].replace('Oyo Rooms','Oyo',inplace=True)
df['StartupName'].replace('Oyorooms','Oyo',inplace=True)
df['StartupName'].replace('OyoRooms','Oyo',inplace=True)
df['StartupName'].replace('OYO Rooms','Oyo',inplace=True)
df['StartupName'].replace('Paytm Marketplace','Paytm',inplace=True)

df=df[(df.InvestmentType=='Seed Funding') | (df.InvestmentType=='Crowd Funding')]

startup=list(df.StartupName)
investor_list=list(df.InvestorsName)

d={}
for i in range(len(investor_list)):
    investor = investor_list[i].split(',')
    for invest in investor:
        invest=invest.strip()
        if (invest != "") and (invest != "Undisclosed Investors"):
            if invest in d:
                s=d[invest]
                s.add(startup[i])
                d[invest]=s
            else:
                d[invest]={startup[i]}

for key in d:
    d[key]=len(d[key])

xaxis=[]
yaxis=[]

for i in d.keys():
        xaxis.append(i)
        yaxis.append(d[i])
# print(xaxis , yaxis)
np_xaxis=np.array(xaxis)
np_yaxis=np.array(yaxis)
np_xaxis=np_xaxis[np.argsort(np_yaxis)]
np_yaxis=np.sort(np_yaxis)
np_xaxis=np_xaxis[len(np_xaxis)-1:len(np_xaxis)-1-5:-1]
np_yaxis=np_yaxis[len(np_yaxis)-1:len(np_yaxis)-1-5:-1]
print(np_xaxis , np_yaxis)
# plt.pie(np_yaxis, labels=np_xaxis, autopct='%.2f%%')
plt.bar(np_xaxis, np_yaxis, color='red')
plt.show()

# investor_list=list(df[df.InvestorsName == 'Private Equity'])
# print()
# d={}
# for i in range(len(investor_list)):
#     investor = investor_list[i].split(',')
#     for invest in investor:
#         invest=invest.strip()
#         if invest != "":
#             if invest in d:
#                 s=d[invest]
#                 s.add(startup[i])
#                 d[invest]=s
#             else:
#                 d[invest]={startup[i]}
#
# print(d)
# for key in d:
#     d[key]=len(d[key])
