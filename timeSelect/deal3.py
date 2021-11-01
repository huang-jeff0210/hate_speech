from numpy.core.fromnumeric import mean
import pandas as pd

df1 = pd.read_csv('../data_fix/莫德納_fix.csv')
df2 = pd.read_csv('../data_fix/輝瑞_fix.csv')

# df = df.groupby('key word')

# az = df.get_group('AZ').reset_index().drop(['index'], axis = 1)
# bnt = df.get_group('bnt').reset_index().drop(['index'], axis = 1)
# mcv = df.get_group('高端').reset_index().drop(['index'], axis = 1)

# az_con3 = az[(az['contents'] == ' 綠共先打') & (az['id'] == 'kilhi')].index.tolist()[0]
# az3 = az.iloc[:az_con3 + 1, :]

# bnt_con3 = bnt[(bnt['contents'].str.contains('真的氣到快哭耶 Q_______Q')) & (bnt['id'] == 'jay0215')].index.tolist()[0]
# bnt3 = bnt.iloc[:bnt_con3 + 1, :]

# az3.to_csv('./output/az.csv', index = False, encoding = 'utf-8-sig')
# bnt3.to_csv('./output/bnt.csv', index = False, encoding = 'utf-8-sig')
# mcv.to_csv('./output/高端.csv', index = False, encoding = 'utf-8-sig')

# az_con5 = az[(az['contents'].str.contains('三樓  總統要打國產疫苗')) & (az['id'] == 'demitri')].index.tolist()[0]
# az5 = az.iloc[:az_con5 + 1, :]

# bnt_con5 = bnt[(bnt['contents'].str.contains('防護衣原料...那些原料')) & (bnt['id'] == 'awayaway')].index.tolist()[0]
# bnt5 = bnt.iloc[:bnt_con5 + 1, :]

# az5.to_csv('./output2/az.csv', index = False, encoding = 'utf-8-sig')
# bnt5.to_csv('./output2/bnt.csv', index = False, encoding = 'utf-8-sig')
# mcv.to_csv('./output2/高端.csv', index = False, encoding = 'utf-8-sig')

df1_con = df1[(df1['contents'] == ' 嬌生 輝瑞') & (df1['id'] == 'iwinlottery')].index.tolist()[0]
df1 = df1.iloc[:df1_con + 1, :]
df2_con = df2[(df2['contents'] == ' 肥宅也不會出門打疫苗') & (df2['id'] == 'hcgcgh911399')].index.tolist()[0]
df2 = df2.iloc[:df2_con + 1, :]

df1.to_csv('../data_fix/莫德納_fix.csv')
df2.to_csv('../data_fix/輝瑞_fix.csv')