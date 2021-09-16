import pandas as pd
import jieba

df = pd.read_csv('D:\學習彙總\python自學\PPT留言\\vaccine\data\疫苗相關all.csv',low_memory=False)
contents = df['contents'].astype(str)

J_sents_annotated_ws = [jieba.lcut(sent,cut_all=False) for sent in contents]

lists = ['AstraZeneca','阿斯特捷利康','BioNTech','Moderna','疫苗','AZ','bnt','輝瑞','高端','莫德納']

sentence = []
for i in range(len(contents)):
    for j in J_sents_annotated_ws[i]:
        for keyword in lists:
            if keyword == j:
                sentence.append(contents[i])


name = ['content']
test = pd.DataFrame(columns=name,data=sentence)
test.to_csv('D:\學習彙總\python自學\PPT留言\\vaccine\select_data\疫苗_select.csv',encoding='utf-8-sig',index=False)

df = pd.read_csv('D:\學習彙總\python自學\PPT留言\\vaccine\select_data\疫苗_select.csv',low_memory=False)
df
df = df.drop_duplicates()
df
df.to_csv('D:\學習彙總\python自學\PPT留言\\vaccine\select_data\疫苗_select.csv',encoding='utf-8-sig',index=False)