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
driver.execute_script('moveMainFrame("0073")')

driver.find_element_by_xpath('//*[@id="meetYear"]')

# 대회년도 별 돌리기
for year in range(2, 11):
    driver.find_element_by_xpath('//*[@id="meetYear"]/option[{}]'.format(year)).click()
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="teamId"]')

    # 12개 구단별 돌리기
    for i in range(1, 11):
        driver.find_element_by_xpath('//*[@id="teamId"]/option[{}]'.format(i)).click()
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        season = soup.select('#searchResult > div.searchResult-group.wid-15p > p')[0].text
        team = soup.select('#searchResult > div:nth-child(5) > p')[0].text

        if team == '상주':
            team = '김천'

        print(team)

        tr = soup.select('#tab-1 > div > div > table > tbody > tr')

        # 구단 별 선수 숫자 돌리기
        for j in range(len(tr)):
            name = soup.select('#tab-1 > div > div > table > tbody > tr:nth-child({}) > td'.format(j + 1))

            # MySQL Connection 연결
            conn = pymysql.connect(host='earlykross.cuopsz9nr7wp.ap-northeast-2.rds.amazonaws.com', user='ek',
                                   password='siattiger',
                                   db='earlykross', charset='utf8')

            curs = conn.cursor()

            # 클럽 번호 뽑아오기
            sql = "select c_id from club where short_name='{}'".format(team)
            curs.execute(sql)
            c_id = curs.fetchone()[0]

            # 클럽번호에 맞는 선수만 뽑아오기
            sql = 'select p_id from player where name=%s and c_id=%s'
            a = curs.execute(sql, (name[0].text, c_id))

            if a == 1:
                p_id = curs.fetchone()[0]

                td = soup.select('#tab-1 > div > div > table > tbody > tr:nth-child({}) > td'.format(j + 1))
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

                print(p_id, td[0].text)

                # SQL문 실행
                sql = '''insert into player_record(p_id, played, played_in, played_out, inout_total, fh_goal, sh_goal, ot_goal, total_goal,
                 assist, gk, ck, fo, os, st, yellow, red, season) 
                 values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s)'''
                curs.execute(sql, (
                    p_id, played, played_in, played_out, inout_total, fh_goal, sh_goal, ot_goal, total_goal, assist, gk,
                    ck,
                    fo, os,
                    st, yellow, red, season))
                conn.commit()

                # Connection 닫기
                conn.close()
