import pandas as pd

df = pd.read_csv('output/hate.csv')
df.insert(0, 'index', df.index, allow_duplicates = False)
df = df.loc[49:, ]

df = df.sample(frac = 0.581, random_state = 41)
print(len(df.index))

df.to_csv('output/hate_sampling.csv', index = False, encoding = 'utf-8-sig')