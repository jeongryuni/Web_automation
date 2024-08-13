import requests
from bs4 import BeautifulSoup
import csv
from openpyxl import Workbook

# csv_file = open('SBS_데이터.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['기간', '순위', '프로그램', '시청률'])

wb = Workbook(write_only=True)


for year in range(2010, 2019):
    ws = wb.create_sheet("{}년".format(year))
    ws.append(['기간', '순위', '프로그램', '시청률'])

    for month in range(1, 13):
        for weekIndex in range(0, 5):
            url = (f'https://workey.codeit.kr/ratings/index?year={year}&month={month}&weekIndex={weekIndex}')
            response = requests.get(url)
            TV_ratings = response.text
            soup = BeautifulSoup(TV_ratings, 'html.parser')
            period = f'{year}년 {month}월 {weekIndex + 1}주'

            tv_ratings_list = []
            for tv_tags in soup.select('tr')[1:]:
                rank = (tv_tags.select('td')[0]).get_text().strip()
                chanel = (tv_tags.select('td')[1]).get_text().strip()
                program = (tv_tags.select('td')[2]).get_text().strip()
                rating = (tv_tags.select('td')[3]).get_text().strip()
                if chanel == 'SBS' :
                    # tv_ratings_list.append([f'{period} {rank}위, {program}, {rating}'])
                    # csv_writer.writerow([period, rank, program, rating])
                    ws.append([period, rank, program, rating])
            # print(tv_ratings_list)
# csv_file.close()
wb.save('SBS_데이터.xlsx')