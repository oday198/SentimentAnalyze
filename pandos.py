import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a=[1,2,3]
myvar=pd.Series(a)
print(myvar)
print(myvar[0])
b=[11,12,13]
myvar2=pd.Series(a,index=['a','b','c'])
print(myvar2)
s=pd.Series([1,2,np.nan,6,7])
print(s)
calories={"day1":20,"day2":150,"day3":700}
myvar3=pd.Series(calories)
print(myvar3)
print(myvar3["day3"])
myvar4=pd.Series(calories,index=["day1","day3"])
print(myvar4)
print(myvar4["day1"])
lst=["Bmw","BENZ","FORD"]
df=pd.DataFrame(lst)
print(df)
df2=pd.DataFrame({"A":1.0,"B":pd.Timestamp("20130102"),"C":pd.Series(1,index=list(range(4)),dtype=float),"D":np.array([3]*4,dtype=int),"E":pd.Categorical(["test","train","test","train"]),"F":"foo"})
print(df2)
mydataset={'cars':["BMW","BENZ","FORD"],'passings':[3,7,2]}
newd=pd.Series(mydataset)
newd2=pd.DataFrame(mydataset)

print(newd)
print("\n")
print(newd2)

data1={"calories":[100,200,300],"duration":[50,60,70]}
data11=pd.DataFrame(data1,index=["day1","day2","day3"])
print(data11)
print(data11.loc["day2"])
print(data11.info())
print("\n")

oday={"cars":["Bnz","BMW","FORD"],"Model":[2015,2020,2024]}
oday1=pd.DataFrame(oday)
print(oday1)
print("\n")
print(oday1.loc[1])
print()
print(oday1.loc[[1]])

