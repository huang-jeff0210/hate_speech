from numpy.core.fromnumeric import mean
import pandas as pd

df = pd.read_csv('../data_fix/阿斯特捷利康_fix.csv')
df_select = df[(df['contents'] == ' 莫德納跟輝瑞對印度變種病毒是一樣的效力嗎？') & (df['id'] == 'bingchuan')].index.tolist()[0]
df = df.iloc[:df_select + 1, :]
df.to_csv('./output/阿斯特捷利康.csv', index = False, encoding = 'utf-8-sig')

df = pd.read_csv('../data_fix/科興_fix.csv')
df_select = df[(df['contents'] == ' 跟樓上想的一樣誰知道是不是木馬屠城天天飛戰機來，台人警覺都變高了') & (df['id'] == 'apatosaurus')].index.tolist()[0]
df = df.iloc[:df_select + 1, :]
df.to_csv('./output/科興.csv', index = False, encoding = 'utf-8-sig')

df = pd.read_csv('../data_fix/國藥_fix.csv')
df_select = df[(df['contents'] == ' 不管效果如何，只要打了沒死人愛國粉就高興死了') & (df['id'] == 'sank')].index.tolist()[0]
df = df.iloc[:df_select + 1, :]
df.to_csv('./output/國藥.csv', index = False, encoding = 'utf-8-sig')

df = pd.read_csv('../data_fix/嬌生_fix.csv')
df_select = df[(df['contents'] == ' 沒買到：政府無能。買到：有副作用不敢打。') & (df['id'] == 'JH10')].index.tolist()[0]
df = df.iloc[:df_select + 1, :]
df.to_csv('./output/嬌生.csv', index = False, encoding = 'utf-8-sig')

df = pd.read_csv('../data_fix/聯亞_fix.csv')
df_select = df[(df['contents'] == ' 唉') & (df['id'] == 'lwei781')].index.tolist()[0]
df = df.iloc[:df_select + 1, :]
df.to_csv('./output/聯亞.csv', index = False, encoding = 'utf-8-sig')

df = pd.read_csv('../data_fix/BioNTech_fix.csv')
df_select = df[(df['contents'] == ' 這很早之前就有的消息，輝瑞的BNT跟復星BNT都是用德國技術製造') & (df['id'] == 'tenka92417')].index.tolist()[0]
df = df.iloc[:df_select + 1, :]
df.to_csv('./output/BioNTech.csv', index = False, encoding = 'utf-8-sig')

df = pd.read_csv('../data_fix/Moderna_fix.csv')
df_select = df[(df['contents'] == ' 美國疫苗已經打過幾億人了...一開始因為不了解怎樣的人會有怎樣的副作用有先例後 施打對象已經有一些限制 對裡面成份過敏不能施打 已經感染過的人三個月內不能打') & (df['id'] == 'k24618099')].index.tolist()[0]
df = df.iloc[:df_select + 1, :]
df.to_csv('./output/Moderna.csv', index = False, encoding = 'utf-8-sig')

df = pd.read_csv('../data_fix/輝瑞_fix.csv')
df_select = df[(df['contents'] == ' 肥宅也不會出門打疫苗') & (df['id'] == 'hcgcgh911399')].index.tolist()[0]
df = df.iloc[:df_select + 1, :]
df.to_csv('./output/輝瑞.csv', index = False, encoding = 'utf-8-sig')

df = pd.read_csv('../data_fix/莫德納_fix.csv')
df_select = df[(df['contents'] == ' 嬌生 輝瑞') & (df['id'] == 'iwinlottery')].index.tolist()[0]
df = df.iloc[:df_select + 1, :]
df.to_csv('./output/莫德納.csv', index = False, encoding = 'utf-8-sig')