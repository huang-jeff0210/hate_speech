from numpy.core.fromnumeric import mean
import pandas as pd

df = pd.read_csv('data_fix/疫苗相關1_fix.csv')


df = df.groupby('key word')

az = df.get_group('AstraZeneca').reset_index().drop(['index'], axis = 1)
az_chinese = df.get_group('阿斯特捷利康').reset_index().drop(['index'], axis = 1)
BioNTech = df.get_group('BioNTech').reset_index().drop(['index'], axis = 1)
Moderna = df.get_group('Moderna').reset_index().drop(['index'], axis = 1)

az_chinese_con = az_chinese[(az_chinese['contents'] == ' 莫德納跟輝瑞對印度變種病毒是一樣的效力嗎？') & (az_chinese['id'] == 'bingchuan')].index.tolist()[0]
az_chinese = az_chinese.iloc[:az_chinese_con + 1, :]

BioNTech_con = BioNTech[(BioNTech['contents'].str.contains(' 菸糞蟑螂：errrrr')) & (BioNTech['id'] == 'villagemen')].index.tolist()[0]
BioNTech = BioNTech.iloc[:BioNTech_con + 1, :]



az.to_csv('timeSelect/output2/AstraZeneca.csv', index = False, encoding = 'utf-8-sig')
az_chinese.to_csv('timeSelect/output2/阿斯特捷利康.csv', index = False, encoding = 'utf-8-sig')
BioNTech.to_csv('timeSelect/output2/BioNTech.csv', index = False, encoding = 'utf-8-sig')
Moderna.to_csv('timeSelect/output2/Moderna.csv', index = False, encoding = 'utf-8-sig')

df1 = pd.read_csv('data_fix/疫苗相關4_fix.csv')
df1.drop('index',axis=1,inplace=True)
df1_con = df1[(df1['contents'].str.contains(' 他是出來帶風向的 公眾人物你當普通大媽？三樓  總統要打國產疫苗')) & (df1['id'] == 'demitri')].index.tolist()[0]
df1 = df1.iloc[:df1_con + 1, :]
df1.to_csv('timeSelect/output2/疫苗.csv', index = False, encoding = 'utf-8-sig')