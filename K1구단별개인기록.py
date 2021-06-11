# 선수개인기록 뽑기
import time
import pymysql

from selenium.webdriver import Edge
from bs4 import BeautifulSoup

# Edge 드라이버 로딩
driver = Edge('driver/msedgedriver.exe')

# 숨겨진 K리그 데이터 포털
driver.get('https://portal.kleague.com/user/loginById.do?portalGuest=rstNE9zxjdkUC9kbUA08XQ==')

# 선수 정보 페이지
driver.execute_script('moveMainFrame("0111")')

driver.find_element_by_xpath('//*[@id="meetYear"]')

# 대회년도 별 돌리기
for year in range(2, 32):
    driver.find_element_by_xpath('//*[@id="meetYear"]/option[{}]'.format(year)).click()
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="teamId"]')

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 모든 구단별 돌리기
    for i in range(1, len(soup.select('#teamId > option')) + 1):
        driver.find_element_by_xpath('//*[@id="teamId"]/option[{}]'.format(i)).click()
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        season = soup.select('#searchResult > div.searchResult-group.wid-15p > p')[0].text
        team = soup.select('#searchResult > div:nth-child(5) > p')[0].text

        print(team)

        tr = soup.select('#tab-1 > div > div > table > tbody > tr')

        # 구단 별 선수 숫자 돌리기
        for j in range(len(tr)):

            # MySQL Connection 연결
            conn = pymysql.connect(host='earlykross.cuopsz9nr7wp.ap-northeast-2.rds.amazonaws.com', user='ek',
                                   password='siattiger',
                                   db='earlykross', charset='utf8')

            curs = conn.cursor()

            td = soup.select('#tab-1 > div > div > table > tbody > tr:nth-child({}) > td'.format(j + 1))

            if len(td) > 1:
                name = td[0].text
                played = td[2].text
                played_in = td[3].text
                played_out = td[4].text
                inout_total = td[5].text
                fh_goal = td[6].text
                sh_goal = td[7].text
                ot_goal = td[8].text
                total_goal = td[9].text
                assist = td[10].text
                gk = td[11].text
                ck = td[12].text
                fo = td[13].text
                os = td[15].text
                st = td[16].text
                yellow = td[21].text
                red = td[22].text

                print(td[0].text)

                # SQL문 실행
                sql = '''insert into player_record_raw(name, club, played, played_in, played_out, inout_total, fh_goal, sh_goal, ot_goal, total_goal,
                 assist, gk, ck, fo, os, st, yellow, red, season)
                 values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s)'''
                curs.execute(sql, (
                    name, team, played, played_in, played_out, inout_total, fh_goal, sh_goal, ot_goal, total_goal, assist,
                    gk,
                    ck, fo, os, st, yellow, red, season))
                conn.commit()

                # Connection 닫기
                conn.close()
