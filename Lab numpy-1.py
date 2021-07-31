
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_table("http://bit.ly/movieusers",sep="|", names=["sr.no","age","gender","profession","views"])
print(df.head())
print(df['gender'])
df['con']=df['age'].map(str)+':'+df['gender'].map(str)
print(df.head())

df.groupby('profession')['age'].nunique().plot(kind='bar')
plt.show()

df.groupby('age')['views'].nunique().plot(kind='bar')
plt.show()

