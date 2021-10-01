import requests, bs4
#'AstraZeneca' 科興,國藥,嬌生,康希諾,聯亞'阿斯特捷利康','BioNTech','Moderna' #'疫苗','AZ','bnt','輝瑞','高端','莫德納',
all_comments = []
for j in range(1,6):
    k = '嬌生'
    url = 'https://www.ptt.cc'
    page = f'/bbs/Gossiping/search?page={j}&q={k}'
    ptthtml = requests.get(url+page,cookies={'over18':'1'})
    soup = bs4.BeautifulSoup(ptthtml.text,'lxml')

    countpost = soup.find_all('div','r-ent')
    print(f'{j}頁')
    for i in range(len(countpost)):
        try:
            href = countpost[i].find('a')['href']
        except:
            pass
        print(f"目前網址 : {url+href}")

        beauty_html = requests.get(url+href,cookies={'over18':'1'})
        beauty_soup = bs4.BeautifulSoup(beauty_html.text,'lxml')
        items = beauty_soup.find_all('div','article-metaline')

        #評論
        comments = beauty_soup.find_all('div','push')
        for comment in comments:
            try:
                person = comment.find('span','f3 hl push-userid').getText()
                content = comment.find('span','f3 push-content').getText().replace(':','')
                date = comment.find('span','push-ipdatetime').getText().replace('\n',' ')
                #print(person,content,date)
                all_comments.append(href+','+person+','+content+','+k+','+date)
            except:
                pass

#print(all_comments)  
         
with open('..\data\嬌生.csv','w',encoding='utf-8-sig') as f:
    for i in all_comments:
        f.write(i.lstrip() + "\n")  