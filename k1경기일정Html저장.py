import time

from selenium.webdriver import Edge
from bs4 import BeautifulSoup

f = open('경기일정.txt', 'r', encoding='utf-8')

driver = Edge('driver/msedgedriver.exe')
for r in f:
    driver.get(r)
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    f_id = r.split('=')[2].replace('&tab', '').replace('\n', '')
    print(f_id)
    with open('일정/{}.html'.format(f_id), 'a', encoding='utf-8') as f:
        f.write(str(soup))
