from selenium.webdriver import Edge
from bs4 import BeautifulSoup

driver = Edge('driver/msedgedriver.exe')

for month in range(2, 8):
    # 2월부터 7월까지
    url = 'https://sports.news.naver.com/kfootball/schedule/index.nhn??category=kleague2?year=2021&month=0{}'.format(
        str(month))
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    compare = soup.select('#_monthlyScheduleList > tr > td.broadcast > div > a:nth-child(1)')

    print(month, '월')
    for i in compare:
        link = 'https://sports.news.naver.com{}'.format(i.attrs['href'])
        print(link)

        with open('경기일정2.txt', 'a', encoding='utf-8') as f:
            f.write(link + '\n')
