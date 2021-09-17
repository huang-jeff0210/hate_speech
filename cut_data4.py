import pandas as pd

df = pd.read_csv('./data/疫苗相關4.csv')

print(df.count())

df1 = df[0:1033187]
df2 = df[1033187:]
df1.to_csv('./data/疫苗相關4_1.csv', index = False, encoding = 'utf-8-sig')
df2.to_csv('./data/疫苗相關4_2.csv', index = False, encoding = 'utf-8-sig')
