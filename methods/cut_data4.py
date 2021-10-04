import pandas as pd

df = pd.read_csv('../select/output/國內外疫苗_select.csv')

print(df.count())

df1 = df.iloc[:80154]
df2 = df.iloc[80154:160307]
df3 = df.iloc[160307:]

df1.to_csv('output/標記1.csv',encoding="utf-8-sig",index=False)
df2.to_csv('output/標記2.csv',encoding="utf-8-sig",index=False)
df3.to_csv('output/標記3.csv',encoding="utf-8-sig",index=False)
