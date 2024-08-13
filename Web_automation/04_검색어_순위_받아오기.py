import requests
from bs4 import BeautifulSoup

response = requests.get('https://workey.codeit.kr/music/index')
music = response.text
soup = BeautifulSoup(music, 'html.parser')


popular_searches = []
search_list = (soup.select('ul.rank__order li'))
for search in search_list:
    popular_searches.append(list(search.stripped_strings)[2])
# 테스트 코드
print(popular_searches)