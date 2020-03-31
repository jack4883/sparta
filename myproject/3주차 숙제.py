import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
# #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis

songs_chart = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
rank = 0


for song in songs_chart:
    title_el = song.select('td.info > a.title.ellipsis')
    artist_el = song.select('td.info > a.artist.ellipsis')

    if len(title_el) > 0:
        rank += 1
        title = title_el[0].text.strip()
        artist = artist_el[0].text.strip()

    print(rank, title, artist)
