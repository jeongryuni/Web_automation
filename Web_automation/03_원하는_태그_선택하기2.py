import requests
from bs4 import BeautifulSoup

# 여기에 코드를 작성하세요
response = requests.get('https://workey.codeit.kr/orangebottle/index')
orange_bottle = response.text
soup = BeautifulSoup(orange_bottle, 'html.parser')

orange_bottle_div = soup.select('div.branch')
orange_bottle_div_select = orange_bottle_div
# print(orange_bottle_div_select)


branch_infos = []
i = 0
while i < len(orange_bottle_div_select):
    branch_name = (orange_bottle_div_select[i].select_one('p.city')).get_text()
    address = (orange_bottle_div_select[i].select_one('p.address')).get_text()
    phone_number = (orange_bottle_div_select[i].select_one('span.phoneNum')).get_text()
    branch_infos.append([branch_name, address, phone_number])
    i = i + 1

print(branch_infos)