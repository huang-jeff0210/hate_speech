import requests, bs4

all_comments = []
for j in range(1,413):
    my_list = ['AZ','bnt','高端']
    for k in my_list:
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
                    #date = comment.find('span','push-ipdatetime').getText().replace('\n',' ')
                    #print(person,content,date)
                    all_comments.append(person+','+content+','+k)
                except:
                    pass
        if j%50 == 0:
            with open('./data/疫苗相關3.csv','a',encoding='utf-8-sig') as f:
                for i in all_comments:
                    f.write(i.lstrip() + "\n")  
            print(f'{j}頁寫入完成')
            all_comments = []
        elif j == 413:
            with open('./data/疫苗相關3.csv','a',encoding='utf-8-sig') as f:
                for i in all_comments:
                    f.write(i.lstrip() + "\n") 
            print('{j}頁寫入完成') 
            all_comments = []