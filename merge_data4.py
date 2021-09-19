import pandas as pd 

df1 = pd.read_csv('./data_fix/疫苗相關4_1_fix.csv')
df2 = pd.read_csv('./data_fix/疫苗相關4_2_fix.csv')

df1 = pd.concat([df1, df2], axis = 0)

df1.to_csv('./data_fix/疫苗相關4_fix.csv')
