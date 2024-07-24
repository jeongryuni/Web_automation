import requests

import main
from bs4 import BeautifulSoup
# beautifulSoup html에서 필요한 정보를 가져와줌

response = requests.get('https://workey.codeit.kr/ratings/index')
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser') # rating_page의 내용을 html.parser로 정리
#print(soup.prettify()) #parser를 사용하여 html코드가 정리가 되어있다.
#print(soup.select('title')) #[<title>티비랭킹닷컴</title>]
#print(soup.select('table')) # select를 이용해 원하는 태그를 가져옴
#print(soup.select('td.program'))


# 프로그램 이름만 가져오기
program_title_tags = soup.select('td.program')

# program_titles = []
# for tag in program_title_tags:
#     program_titles.append(tag.get_text())
#
# print(program_titles)

# 매칭되는 태그를 하나만 가져오기, 가장위에 나타나는 태그를 가져옴
print(soup.select_one('td.program'))