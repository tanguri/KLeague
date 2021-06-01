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
driver.execute_script('moveMainFrame("0053")')

driver.find_element_by_xpath('//*[@id="meetYear"]')

for year in range(2, 11):
    driver.find_element_by_xpath('//*[@id="meetYear"]/option[{}]'.format(year)).click()
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="teamId"]')

    for i in range(1, 13):
        driver.find_element_by_xpath('//*[@id="teamId"]/option[{}]'.format(i)).click()
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        year = soup.select('#searchResult > div.searchResult-group.wid-15p > p')[0].text
        team = soup.select('#searchResult > div:nth-child(5) > p')[0].text

        name = soup.select('#tab-1 > div > div > table > tbody > tr:nth-child(1) > td')

        # MySQL Connection 연결
        conn = pymysql.connect(host='earlykross.cuopsz9nr7wp.ap-northeast-2.rds.amazonaws.com', user='ek',
                               password='siattiger',
                               db='earlykross', charset='utf8')

        curs = conn.cursor()

        sql = 'select p_id from player where name=%s'
        n = curs.execute(sql, (1, name[0].text))

        print(n)



