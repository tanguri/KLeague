import time
import pymysql
from bs4 import BeautifulSoup
from selenium.webdriver import Edge

driver = Edge('driver/msedgedriver.exe')
driver.get('https://m.sports.naver.com/game/20210606170990/relay')
time.sleep(3)

ha = driver.find_element_by_xpath('//*[@id="content"]/div/div/section[2]/div[2]/div[2]/div[2]/h3/a')
ha.click()
time.sleep(1)
# 더보기 계속 클릭하기
while True:
    try:
        more1 = driver.find_element_by_xpath('//*[@id="content"]/div/div/section[2]/div[2]/div[2]/div[1]/div/a')
        more1.click()
        time.sleep(1)
    except:
        break

while True:
    try:
        more2 = driver.find_element_by_xpath('//*[@id="content"]/div/div/section[2]/div[2]/div[2]/div[2]/div/a')
        more2.click()
        time.sleep(1)
    except:
        break

time.sleep(1)

soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup.select('.TimeLine_inner__1JnKT'))

times = []
texts = []

for t in soup.select('.TimeLine_time__11YMk'):
    times.append(t.text)

for t in soup.select('.TimeLine_inner__1JnKT'):
    texts.append(t.text)

# MySQL Connection 연결
conn = pymysql.connect(host='localhost', user='ek',
                       password='ek',
                       db='earlykross', charset='utf8')

f_id = 20210606170990

for time, text in zip(times, texts):
    sql = 'insert into relay(f_id, r_date, r_text) values (%s, %s, %s)'

    curs = conn.cursor()
    curs.execute(sql, (f_id, time, text))
    conn.commit()

conn.close()
