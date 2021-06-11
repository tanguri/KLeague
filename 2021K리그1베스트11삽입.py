from selenium.webdriver import Edge
from bs4 import BeautifulSoup

driver = Edge('driver/msedgedriver.exe')
driver.get('https://namu.wiki/w/K%EB%A6%AC%EA%B7%B81/2021%EB%85%84')
driver.find_elements_by_xpath('//*[@id="app"]/div/div[2]/article/div[3]/div[2]/div/div/div[21]/div[2]/table/tbody')


soup = BeautifulSoup(driver.page_source, 'html.parser')

print(soup)

