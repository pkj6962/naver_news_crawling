from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import bs4



"""
Input: 특정 기사 URL(네이버)(type: str)
Output: 기사 관련 크롤링 데이터(type: dict) 

헤드라인, 언론사, 기사작성일, 기사 본문, 이미지, 요약(기사 초두에 볼드체로 표시되는 n줄 요약) 크롤링하는 함수
"""

def new_article(url):


    page = urlopen(url)
    soup  = bs(page, 'html.parser')
    fp = open("page.txt", "w")

    summary = ""
    img_url = []
    main_content = ""

    metadata = soup.find("div", class_= "media_end_head")
    press = metadata.find("img").attrs['title']
    headline = metadata.find("h2").contents[0]
    date = metadata.find(class_="media_end_head_info_datestamp_time").attrs['data-date-time'].split()[0]
    journalist = metadata.find(class_="media_end_head_journalist_name").contents[0]


    content = soup.find("div", id="dic_area")
    for element in content:
        try: 
            if element.name == 'span':          # 이미지가 저장되어 있는 태그 
                img = element.find("img")
                img_url.append(img.attrs['data-src'])
            elif element.name == 'b':           # 요약글이 저장되어 있는 태그 
                summary = '\n\n'.join(line for line in element.contents if type(line) is not bs4.element.Tag)
            elif element.name == 'br':          
                continue 
            else:                               # 문단                               
                main_content += element + '\n\n'
        except:
            pass

    
    article_data = {'press':press, 'headline': headline, 'date': date, 
        'journalist': journalist, 'main_content': main_content, 'img_url': img_url, 'summary':summary}

    
    return article_data


if __name__ == "__main__":
    url = "https://n.news.naver.com/mnews/article/310/0000098949?sid=102"
    new_article(url)
