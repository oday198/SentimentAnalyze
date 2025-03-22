import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\User\Desktop\data12.csv")
print(df)
print("\n")
print(df["Calories"])
newdf=df.iloc[:8,1:3]
print("\n")
print(newdf)
print(df.iloc[:4,:1])
print(df.corr())
df.plot()

plt.show()