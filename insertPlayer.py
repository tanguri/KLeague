import os
import pymysql
from bs4 import BeautifulSoup

# MySQL Connection 연결
conn = pymysql.connect(host='earlykross.cuopsz9nr7wp.ap-northeast-2.rds.amazonaws.com', user='ek', password='siattiger',
                       db='earlykross', charset='utf8')

path = 'player'
file_list = os.listdir(path)
file_list_html = [file for file in file_list if file.endswith(".html")]

for f in file_list_html:
    file = open('player/{}'.format(f), 'r', encoding='utf-8')

    soup = BeautifulSoup(file, 'html.parser')

    name = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2)').text.strip()

    name = name[:name.find('(') - 1]
    ename = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(4)').text.strip()
    c_id = f[-7:-5]
    p_id = f[5:13]

    position = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)').text.strip()
    back_no = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)').text.strip()
    nationality = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(4)').text.strip()
    height = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(4) > td:nth-child(2)').text.strip()
    weight = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(4) > td:nth-child(4)').text.strip()
    birthday = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(5) > td.bar_bottm_right.taL.pl10').text.strip()

    print(int(c_id), int(p_id), name, ename, position, back_no, nationality, height, weight, birthday)

    # Connection 으로부터 Cursor 생성
    curs = conn.cursor()

    # SQL문 실행
    sql = 'insert into player(back_no, birthday, ename, height, name, nationality, position, weight, c_id, ' \
          'p_id) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) '

    curs.execute(sql, (back_no, birthday, ename, height, name, nationality, position, weight, int(c_id), int(p_id)))
    conn.commit()

    # Connection 닫기
conn.close()
