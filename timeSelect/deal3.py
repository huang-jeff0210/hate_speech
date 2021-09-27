from numpy.core.fromnumeric import mean
import pandas as pd

df = pd.read_csv('../data_fix/疫苗相關3_fix.csv')

df = df.groupby('key word')

az = df.get_group('AZ').reset_index().drop(['index'], axis = 1)
bnt = df.get_group('bnt').reset_index().drop(['index'], axis = 1)
mcv = df.get_group('高端').reset_index().drop(['index'], axis = 1)

az_con = az[(az['contents'] == ' 綠共先打') & (az['id'] == 'kilhi')].index.tolist()[0]
az = az.iloc[:az_con + 1, :]

bnt_con = bnt[(bnt['contents'].str.contains('真的氣到快哭耶 Q_______Q')) & (bnt['id'] == 'jay0215')].index.tolist()[0]
bnt = bnt.iloc[:bnt_con + 1, :]

az.to_csv('./output/az.csv', index = False, encoding = 'utf-8-sig')
bnt.to_csv('./output/bnt.csv', index = False, encoding = 'utf-8-sig')
mcv.to_csv('./output/高端.csv', index = False, encoding = 'utf-8-sig')
