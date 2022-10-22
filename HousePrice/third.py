import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#########
# just try pandas
#########

# print(pd.__version__)
# %%
# cadata = open("C:/Users/lxanas/Desktop/DS_Practice/attention/HousePrice/cadata.csv", 'r')
# cadata = [x.rstrip() for x in cadata]
# # print(cadata)
# ndata = []
# for x in cadata:
#     ndata.append([x])
# # print(ndata[0])
# data = pd.DataFrame(ndata[1:],columns=ndata[0])
# print(data)

# %%
df = pd.read_csv("C:/Users/lxanas/Desktop/DS_Practice/attention/HousePrice/data_for_analysis.csv")
# ndf = pd.DataFrame((df['median house value'],df['median income'],df["households"]),index=df['block group ID'])
# print(ndf.mean())
ndf = pd.DataFrame()
ndf['median house value'] = df['median house value']
ndf['median income'] = df['median income']
ndf['households'] = df['households']
print(ndf.mean(), end='\n\n')
print(ndf.var(), end='\n\n')
print(ndf.mode().iloc[0], end='\n\n')
print(ndf.skew(), end='\n\n')

ndf2 = pd.DataFrame()
ndf2['housing median age'] = df['housing median age']
ndf2['total rooms'] = df['total rooms']
ndf2['population'] = df['population']

plt.hist(ndf2['housing median age'])
plt.show()

plt.hist(ndf2['total rooms'])
plt.show()

plt.hist(ndf2['population'])
plt.show()

plt.scatter(df['median income'],df['median house value'])
plt.show()

plt.scatter(df['total rooms'],df['median house value'])
plt.show()

plt.scatter(df['population'],df['median house value'])
plt.show()