import pandas as pd
#import jieba

df = pd.read_csv('D:\學習彙總\python自學\PPT留言\\vaccine\select_data\疫苗_select.csv',low_memory=False)
contents = df['content'].astype(str)

df = df[~ df['content'].str.contains('聖蟑士|柯文哲|柯P|阿北|小英|蔡英文|二毛|五毛|支那|共匪|小粉紅|吱吱|時代力量|菸粉|1450|側翼|中共|黨|KMT|DPP|綠共|綠狗|塔綠班|藍|綠|白|4%|四趴',case=False)]

df = df[df['content'].str.len()<15]
df

df = df[df['content'].str.len()>15]
df

df.to_csv('D:\學習彙總\python自學\PPT留言\\vaccine\select_data\疫苗_select2.csv',index=False)
