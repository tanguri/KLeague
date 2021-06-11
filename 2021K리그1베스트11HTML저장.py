from selenium.webdriver import Edge
from bs4 import BeautifulSoup

driver = Edge('driver/msedgedriver.exe')
driver.get('https://namu.wiki/w/K%EB%A6%AC%EA%B7%B81/2021%EB%85%84')

soup = BeautifulSoup(driver.page_source, 'html.parser')

with open('2021K리그1베스트11.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
