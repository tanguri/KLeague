from selenium.webdriver import Edge
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

# Edge 드라이버 로딩
driver = Edge('driver/msedgedriver.exe')

# K리그 기록실
driver.get('https://www.kleague.com/record?ch=083504')

driver.find_element_by_xpath('//*[@id="pills-history-tab"]').click()
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="select_history_type"]').click()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="select_history_type"]/option[3]').click()
driver.implicitly_wait(1)

# 시즌 누르고
driver.find_element_by_xpath('//*[@id="select_history_year"]')

soup = BeautifulSoup(driver.page_source, 'html.parser')

season = len(soup.select('#select_history_year > option'))

for s in range(season):
    driver.find_element_by_xpath('//*[@id="select_history_year"]/option[{}]'.format(s + 1)).click()
    # 대회 누르고
    soup.select('#select_history_competition')
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    a = soup.select('#select_history_competition > option')

    for i in a:
        print(i)
# for i in ss:
#     # print(i.attr['value'])
#
#     print(i['value'])
