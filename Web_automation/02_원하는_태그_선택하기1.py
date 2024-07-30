import requests
from bs4 import BeautifulSoup

requests = requests.get('https://workey.codeit.kr/orangebottle/index')
phone_number = requests.text
soup = BeautifulSoup(phone_number, 'html.parser')


phone_number = soup.select('span.phoneNum')

phone_numbers = []
for number in phone_number:
    phone_numbers.append(number.get_text())

# 테스트 코드
print(phone_numbers)