import time

from bs4 import BeautifulSoup
from selenium.webdriver import Edge

# import requests
# r = requests.get('https://m.sports.naver.com/game/20210606080588/relay')

driver = Edge('driver/msedgedriver.exe')
driver.get('https://m.sports.naver.com/game/20210606080588/relay')
time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')

print(soup)
