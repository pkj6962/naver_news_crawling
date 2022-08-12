from urllib.request import urlopen
from bs4 import BeautifulSoup

fp = open("page.txt", "w")

topic = {'정치': 100, '경제': 101, '사회': 102}


page = urlopen(
    "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100")


soup = BeautifulSoup(page, "html.parser")

news_class = "cluster_item"  # 기사 하나에 대한 정보가 담긴 클래스 이름

for li in soup.find_all("li", news_class):
    if 'as_line' in li.attrs['class']:
        continue
    else:
        anchor = li.find("a")
        print(anchor.attrs['href'])


# for tag in soup.select('div.cluster_text > a'):
#     print(tag)

# cluster_item 은 포함시키고, 그 중에서 as_line은 제외시킨다.

# print(soup)

# for object in bsOmxdabject.find_all("div", class_="cluster_text"):
#     print(object)


# fp.write(str(bsObject))
