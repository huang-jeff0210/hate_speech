import pandas as pd

df = pd.read_csv('output\疫苗_select1.csv',low_memory=False)
df
df['contents'] = df['contents'].astype(str)

df = df[~ df['contents'].str.contains('對岸|中共|聖蟑士|柯文哲|柯P|阿北|小英|蔡英文|二毛|五毛|支那|共匪|小粉紅|吱吱|時代力量|菸粉|1450|側翼|中共|黨|KMT|DPP|綠共|綠狗|塔綠班|藍|綠|白|4%|四趴',case=False)]
df

# df = df[(df['contents'].str.len()>10) & (df['contents'].str.len()<25)]
# df
# df.to_csv('D:\學習彙總\python自學\PPT留言\\vaccine\select_data\疫苗_select_fix2.csv',index=False)



df2 = df[ df['contents'].str.contains('高端|聯亞|科興|國藥|嬌生|康希諾|AstraZeneca|阿斯特捷利康|BioNTech|Moderna|AZ|bnt|輝瑞|莫德納',case=False)]
df2 = df2[~ df2['contents'].str.contains('http|png|jpg',case=False)]
df2
df2.to_csv('output\國內外疫苗_select.csv',index=False)

