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

driver.find_element_by_xpath('//*[@id="teamId"]')

soup = BeautifulSoup(driver.page_source, "html.parser")

def name(x):
    return {
        '울산': 1, '수원': 2, '포항': 3, '제주': 4, '전북': 5, '부산': 6, '전남': 7, '성남': 8, '서울': 9, '대전': 10, '대구': 17, '인천': 18,
        '경남': 20, '강원': 21, '광주': 22, '부천': 26, '안양': 27, '수원FC': 29, '서울E': 31, '안산': 32, '충남아산': 34, '김천': 35}[x]

# 모든 구단별 돌리기
for i in range(1, len(soup.select('#teamId > option')) + 1):
    driver.find_element_by_xpath('//*[@id="teamId"]/option[{}]'.format(i)).click()
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    team = soup.select('#searchResult > div:nth-child(5) > p')[0].text

    with open('2021구단별기록K2/{}.html'.format(name(team)), 'a', encoding='utf-8') as f:
        f.write(str(soup))
