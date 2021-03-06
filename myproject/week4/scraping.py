import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
movie_info = soup.select('#old_content > table > tbody > tr')
rank = 0

# movies (tr들) 의 반복문을 돌리기

for movie in movie_info:
    title_el = movie.select('a')
    point_el = movie.select('td.point')
    if len(title_el) > 0:
        rank += 1
        title = title_el[0].text
        point = point_el[0].text

        print(rank,title,point)


    # print(title)