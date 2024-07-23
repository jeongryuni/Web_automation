import requests

response = requests.get("https://google.com")
# print(response) #<Response [200]> 요청성공
# print(response.text)

#https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex=0

rating_pages=[]
for i in range(5):
    url = "https://workey.codeit.kr/ratings/index?year=2010&month=1&weekIndex={}".format(i)
    print(url)
    response = requests.get(url)
    rating_page = response.text
    rating_pages.append(rating_page)
print(len(rating_pages))
print(rating_pages[0])