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
driver.execute_script('moveMainFrame("0126")')

driver.find_element_by_xpath('//*[@id="teamId"]')

soup = BeautifulSoup(driver.page_source, "html.parser")

'''
    private String pMg; // 최다득점선수
    private String pMa; // 최다도움선수
    private String pMap; // 최다공포선수
    private String pMp; // 최다출장선수
    
    private int mostGoal; // 최다득점수
    private int mostAs; // 최다도움수
    private int mostAp; // 최다공격포인트수
    private int mostPlayed; // 최다출장수
'''

pMg = ''
pMa = ''
pMap = ''
pMp = ''

mostGoal = 0
mostAs = 0
mostAp = 0
mostPlayed = 0

def name(x):
    return {
        '울산': 1, '수원': 2, '포항': 3, '제주': 4, '전북': 5, '부산': 6, '전남': 7, '성남': 8, '서울': 9, '대전': 10, '대구': 17, '인천': 18,
        '경남': 20, '강원': 21, '광주': 22, '부천': 26, '안양': 27, '수원FC': 29, '서울E': 31, '안산': 32, '충남아산': 34, '김천': 35}[x]


# 모든 구단별 돌리기
for i in range(2, len(soup.select('#teamId > option')) + 1):
    driver.find_element_by_xpath('//*[@id="teamId"]/option[{}]'.format(i)).click()
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # c_id 추출
    team_name = name(soup.select('#searchResult > div:nth-child(3) > p')[0].text)

    print(team_name)
    driver.find_elements_by_xpath('//*[@id="record"]')

    '''
        1. 득점
        2. 도움
        3. 공격포인트
        15. 출전
    
    '''
    driver.find_element_by_xpath('//*[@id="record"]/option[{}]'.format(1)).click()
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 최다 득점 선수
    pMg = soup.select('#tab-1 > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2)')[0].text

