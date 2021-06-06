import time

from selenium.webdriver import Edge
from bs4 import BeautifulSoup
import pymysql

f = open('경기일정.txt', 'r', encoding='utf-8')

driver = Edge('driver/msedgedriver.exe')
for r in f:
    driver.get(r)

    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    f_id = r.split('=')[2].replace('&tab', '').replace('\n', '')
    date = soup.select('#content > div > div > section > div > div:nth-child(1) > p:nth-child(2)')
    stadium = soup.select('#content > div > div > section > div > div:nth-child(1) > p:nth-child(3)')
    home = soup.select(
        '#content > div > div > section > div > div:nth-child(2) > div > div:nth-child(2) > em')
    away = soup.select(
        '#content > div > div > section > div > div:nth-child(3) > div > div:nth-child(2) > em')

    day = date[0].text[:5]
    time = date[0].text[5:]
    home_team = home
    away_team = away
    stadium_name = stadium

    # print(f_id, home_team, away_team, stadium_name)
    print(f_id, day, time, home_team, away_team, stadium_name)

    # # MySQL Connection 연결
    # conn = pymysql.connect(host='earlykross.cuopsz9nr7wp.ap-northeast-2.rds.amazonaws.com', user='ek', password='siattiger',
    #                        db='earlykross', charset='utf8')
    #
    # curs = conn.cursor()
    #
    # # SQL문 실행
    # sql = 'insert into league(season, league, rank, c_id, played, points, won, drawn, lost, gf, ga, gd, assist, fo) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    #
    # curs.execute(sql, (season, league, rank, team_name, played, points, won, drown, lost, gf, ga, gd, assist, fo))
    # conn.commit()
