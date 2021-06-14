import pymysql
from bs4 import BeautifulSoup
import os

# MySQL Connection 연결
conn = pymysql.connect(host='earlykross.cuopsz9nr7wp.ap-northeast-2.rds.amazonaws.com', user='ek',
                       password='siattiger',
                       db='earlykross', charset='utf8')

path = "일정"
file_list = os.listdir(path)
file_list_html = [file for file in file_list if file.endswith(".html")]

def name(x):
    return {
        '울산': 1, '수원': 2, '포항': 3, '제주': 4, '전북': 5, '부산': 6, '전남': 7, '성남': 8, '서울': 9, '대전': 10, '대구': 17, '인천': 18,
        '경남': 20, '강원': 21, '광주': 22, '부천': 26, '안양': 27, '수원FC': 29, '서울E': 31, '안산': 32, '충남아산': 34, '김천': 35}[x]


for file in file_list_html:
    f = open('일정/{}'.format(file), 'r', encoding='utf-8')

    f_id = file.replace('.html', ' ')

    soup = BeautifulSoup(f, 'html.parser')

    date = soup.select('#content > div > div > section > div > div:nth-child(1) > p:nth-child(2)')
    stadium = soup.select('#content > div > div > section > div > div:nth-child(1) > p:nth-child(3)')
    home = soup.select(
        '#content > div > div > section > div > div:nth-child(2) > div > div:nth-child(2) > em')
    away = soup.select(
        '#content > div > div > section > div > div:nth-child(3) > div > div:nth-child(2) > em')

    day = date[0].text[:5]
    time = date[0].text[5:]
    daytime = '2021-{} {}'.format(day.replace('.', '-'), time)
    home_team = home[0].text
    away_team = away[0].text
    stadium_name = stadium[0].text

    print(f_id, daytime, home_team, away_team, stadium_name)

    curs = conn.cursor()

    # SQL문 실행
    sql = 'insert into fixture(f_id, f_date, home, away, stadium) values (%s, %s, %s, %s, %s)'

    curs.execute(sql, (int(f_id), daytime, name(home_team), name(away_team), stadium_name))
    conn.commit()

conn.close()
