import pandas as pd

df = pd.read_csv('./data/疫苗相關4_2.csv')

df['contents'] = df['contents'].astype('str')

fix = pd.DataFrame()
df_fix = pd.DataFrame()

for index, row in df.iterrows():
    try:
        if row['id'] == df.loc[index + 1, 'id']:
            df.loc[index + 1, 'contents'] = row['contents'] + df.loc[index + 1, 'contents'].lstrip()
        elif row['id'] != df.loc[index + 1, 'id']:
            for i in row.index:
                fix.loc[0, i] = row[i]
            df_fix = pd.concat([df_fix, fix], axis = 0)
    except:
        for i in row.index:
            fix.loc[0, i] = row[i]
        df_fix = pd.concat([df_fix, fix], axis = 0)

df_fix.to_csv('./data_fix/疫苗相關4_2_fix.csv', index = False, encoding = 'utf-8-sig')



