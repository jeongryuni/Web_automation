import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import csv

csv_file = open('오렌지_보틀.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['지점 이름', '주소', '전화번호'])


# HTML 코드 받아오기
response = requests.get("https://workey.codeit.kr/orangebottle/index")

# BeautifulSoup 사용해서 HTML 코드 정리
soup = BeautifulSoup(response.text, 'html.parser')
branch_infos = []

# 모든 지점에 대한 태그 가져오기
branch_tags = soup.select('div.branch')

for branch_tag in branch_tags:
    # 각 태그에서 지점 이름, 전화번호 가져오기
    branch_name = branch_tag.select_one('p.city').get_text()
    address = branch_tag.select_one('p.address').get_text()
    phone_number = branch_tag.select_one('span.phoneNum').get_text()
    csv_writer.writerow([branch_name, address, phone_number])

csv_file.close()
