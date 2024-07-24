import main
import requests

response = requests.get("https://google.com")
# print(response) #<Response [200]> 요청성공
# print(response.text)

#https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0
#
# rating_pages=[]
# for i in range(5):
#     url = "https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex={}".format(i)
#     print(url)
#     response = requests.get(url)
#     rating_page = response.text
#     rating_pages.append(rating_page)
# print(len(rating_pages))
# print(rating_pages[0])



import main

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