import pandas as pd 

df1 = pd.read_csv('output/標記1.csv')
df2 = pd.read_csv('output/標記2.csv')
df3 = pd.read_csv('output/標記3.csv')


df1 = pd.concat([df1, df2, df3], axis = 0)

df1.to_csv('./data_fix/疫苗相關4_fix.csv',index=False)
