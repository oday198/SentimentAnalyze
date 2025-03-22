import pandas as pd
import matplotlib.pyplot as plt
df1=pd.read_csv(r'C:\Users\User\Downloads\data.csv')
print(df1)
for x in df1.index:
    if df1.loc[x,'Duration']>120:
        df1.drop(x,inplace=True)

df1.loc[7,'Duration']=45

print(df1.isnull().sum())
for x in df1.index:
    if df1.loc[x,'Calories']>400:
        df1.loc[x,'Calories']=400
print(df1)

print(df1.duplicated())
df1.drop_duplicates(subset='Duration')

df1.drop_duplicates(inplace=True)
print(df1)
df1.plot()
plt.show()
x=df1["Duration"]

y=df1["Calories"]
plt.scatter(x,y)
plt.show()

plt.subplot(1,2,1)
plt.scatter(df1['Pulse'],df1['Maxpulse'])

plt.subplot(1,2,2)
plt.bar(df1['Pulse'],df1['Maxpulse'])
plt.show()