import pandas as pd

<<<<<<< HEAD
df = pd.read_csv('../data/AZ.csv', names = ['href', 'id', 'contents', 'key', 'date'], low_memory=False)
=======
df = pd.read_csv('../data/bnt.csv', names = ['href', 'id', 'contents', 'key', 'date'])
>>>>>>> tomato_fix_data

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

df_fix['contents_order'] = df_fix['contents'].groupby(df_fix['href']).transform(lambda x: range(1, len(x)+1))
print(df_fix['contents_order'])

df_fix.to_csv('../data_fix/AZ_fix.csv', index = False, encoding = 'utf-8-sig')



