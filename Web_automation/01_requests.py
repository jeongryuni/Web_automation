'''
실습 설명
티비랭킹닷컴 사이트에서 처음 3년(2010~2012)간의 데이터를 가져와 주세요.

웹사이트 주소의 구조를 활용해서, 모든 페이지의 HTML 코드를 rating_pages에 저장해 주세요.

2010년 1월부터 2012년 12월까지 모든 달에 대해, 1주차~5주차 페이지를 순서대로 리스트에 넣어주시면 됩니다.

이전 레슨에서 봤듯이, 5주차가 없는 달은 데이터가 없는 페이지가 나오는데요. 그런 페이지들도 리스트에 넣어주세요.

'''

import requests

response = requests.get("https://google.com")
# print(response) #<Response [200]> 요청성공
# print(response.text)

#https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0
#


rating_pages = []
for i in range(2010, 2013):
    for j in range(1, 13):
        for k in range(0,5):
            url = f"https://workey.codeit.kr/ratings/index?year={i}&month={j}&weekIndex={k}"
            response = requests.get(url)
            rating_page = response.text
            rating_pages.append(rating_page)

# 테스트 코드
print(len(rating_pages)) # 가져온 총 페이지 수
print(rating_pages[0]) # 첫 번째 페이지의 HTML 코드