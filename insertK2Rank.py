# https://sports.news.naver.com/kfootball/record/index.nhn?category=kleague&year=2021

from bs4 import BeautifulSoup
import requests
import pymysql

# MySQL Connection 연결
conn = pymysql.connect(host='earlykross.cuopsz9nr7wp.ap-northeast-2.rds.amazonaws.com', user='ek', password='siattiger',
                       db='earlykross', charset='utf8')

league = 'kleague2'
season = '2021'
url = 'https://sports.news.naver.com/kfootball/record/index.nhn?category={}&year={}'.format(league, season)

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

tr = soup.select('#regularGroup_table > tr')


def name(x):
    return {
        '울산': 1, '수원': 2, '포항': 3, '제주': 4, '전북': 5, '부산': 6, '전남': 7, '성남': 8, '서울': 9, '대전': 10, '대구': 17, '인천': 18,
        '경남': 20, '강원': 21, '광주': 22, '부천': 26, '안양': 27, '수원FC': 29, '서울E': 31, '안산': 32, '충남아산': 34, '김천': 35}[x]


for i in range(1, len(tr) + 1):
    rank = soup.select('#regularGroup_table > tr:nth-child({}) > th > strong'.format(i))[0].text
    team_name = soup.select('#regularGroup_table > tr:nth-child({}) > td.tm > div > span'.format(i))[0].text
    print(team_name)
    team_name = name(team_name)
    played = soup.select('#regularGroup_table > tr:nth-child({}) > td:nth-child(3)'.format(i))[0].text
    points = soup.select('#regularGroup_table > tr:nth-child({}) > td:nth-child(4) > strong'.format(i))[0].text
    won = soup.select('#regularGroup_table > tr:nth-child({}) > td:nth-child(5)'.format(i))[0].text
    drown = soup.select('#regularGroup_table > tr:nth-child({}) > td:nth-child(6)'.format(i))[0].text
    lost = soup.select('#regularGroup_table > tr:nth-child({}) > td:nth-child(7)'.format(i))[0].text
    gf = soup.select('#regularGroup_table > tr:nth-child({}) > td:nth-child(8)'.format(i))[0].text
    ga = soup.select('#regularGroup_table > tr:nth-child({}) > td:nth-child(9)'.format(i))[0].text
    gd = soup.select('#regularGroup_table > tr:nth-child({}) > td:nth-child(10)'.format(i))[0].text
    assist = soup.select('#regularGroup_table > tr:nth-child({}) > td:nth-child(11)'.format(i))[0].text
    fo = soup.select('#regularGroup_table > tr:nth-child({}) > td:nth-child(12)'.format(i))[0].text

    print(rank, team_name, played, points, won, drown, lost, gf, ga, gd, assist, fo)

    curs = conn.cursor()

    # SQL문 실행
    sql = 'insert into league(season, league, rank, c_id, played, points, won, drawn, lost, gf, ga, gd, assist, fo) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

    curs.execute(sql, (season, league, rank, team_name, played, points, won, drown, lost, gf, ga, gd, assist, fo))
    conn.commit()

# Connection 닫기
conn.close()
