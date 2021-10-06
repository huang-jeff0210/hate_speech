import pandas as pd

df = pd.read_csv('output\標記1.csv',low_memory=False)
df
df['contents'] = df['contents'].astype(str)

df = df[~ df['contents'].str.contains('amazon',case=False)]
df

df.to_csv('output\標記1.csv',index=False,encoding='utf-8-sig')

