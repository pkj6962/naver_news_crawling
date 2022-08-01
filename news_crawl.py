from urllib.request import urlopen
from bs4 import BeautifulSoup as bs 



"""
Input: 특정 기사 URL(네이버)(type: str)
Output: 기사 관련 크롤링 데이터(type: dict) 

기사 본문, 이미지, 요약(기사 초두에 볼드체로 표시되는 n줄 요약) 크롤링하는 함수
(기사 제목, 기자 이름, 언론사 등 메타 정보도 크롤링해서 리턴값에시켜야 함)
"""

def new_article(url):


    page = urlopen(url)
    soup  = bs(page, 'html.parser')
    fp = open("page.txt", "w")

    summary = ""
    img_url = []
    main_content = ""

    content = soup.find("div", id="dic_area")
    for element in content:
        try: 
            if element.name == 'span':          # 이미지가 저장되어 있는 태그 
                img = element.find("img")
                img_url.append(img.attrs['data-src'])
            elif element.name == 'b':           # 부제가 저장되어 있는 태그 
                summary += element.contents + '\n\n'
            elif element.name == 'br':          
                continue 
            else:                               # 문단                               
                main_content += element + '\n\n'
        except:
            pass

    
    article_data = {'main_content': main_content, 'img_url': img_url, 'summary':summary}


    return article_data


if __name__ == "__main__":
    url = "https://n.news.naver.com/mnews/article/629/0000163463"
    new_article(url)
