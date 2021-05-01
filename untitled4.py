import torch
import pandas as pd
import numpy as np

df1 = pd.read_csv("train.csv")
print(df1.describe())
print(df1.isnull().sum())
print(df1.isnull())
print(df1.columns)
df_null = df1.isnull()
df1[df_null == True]
# df1.describe()
print(df1[['Age']].describe())

print(df1.drop(['Ticket','Embarked'], axis = 1))
df1 = df1.drop(['Ticket','Embarked','Name'], axis = 1)
print(df1)