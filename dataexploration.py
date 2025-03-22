import pandas as pd
dataframe1=pd.read_csv(r'C:\Users\User\Downloads\data.csv')
print(dataframe1)
print("\n")
print(dataframe1.info())
print("\n")
print(dataframe1.describe())
print(dataframe1.shape)
print(dataframe1.values)
print("\n")
print(dataframe1["Duration"])
print(dataframe1.loc[dataframe1["Duration"]==75])
print(dataframe1.loc[0:2,["Duration","Calories"]])
print("\n")
print(dataframe1.iloc[5])
print(dataframe1[["Duration","Calories","Pulse"]].head(4))
index2=dataframe1.index[dataframe1["Duration"]==75]
df2=dataframe1.loc[index2]
print(df2)
dataframe1.drop(150,inplace=True)
print(dataframe1)
dataframe1.drop(dataframe1.index[4:6],inplace=True)
print(dataframe1)
dataframe1.columns=["DURATION","PULSE","MAXIMUMPULSE","CALORIES"]
print(dataframe1)
dataframe1.rename(columns={"CALORIES":"cal"},inplace=True)
print(dataframe1)
x=dataframe1.drop(columns=["PULSE"],axis=1)
print(x.head())
dataframe1.loc[1,"DURATION"]=75
print(dataframe1.head())
dataframe1.loc[0:2,["DURATION","cal"]]=[100,400.0]
print(dataframe1.head())
print("\n")
print(dataframe1.corr())
print("\n")
print(dataframe1.isnull().sum())
print("\n")
dataframe1.dropna(subset=['DURATION'],inplace=True)
print("\n")
x=dataframe1["cal"].mean()
dataframe1['cal'].fillna(x,inplace=True)


print("calculate mode and replace any empty values with it")
y=dataframe1["DURATION"].mode()[0]
dataframe1["DURATION"].fillna(y,inplace=True)
print(dataframe1)
print(dataframe1.dtypes)


