# https://sports.news.naver.com/kfootball/record/index.nhn?category=kleague&year=2021

from bs4 import BeautifulSoup
import requests

url = 'https://sports.news.naver.com/kfootball/record/index.nhn?category=kleague&year=2021'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

tr = soup.select('#regularGroup_table > tr')

# rank = soup.select('#regularGroup_table > tr > th > strong')
# team_name = soup.select('#regularGroup_table > tr > td.tm > div > span')
# game = soup.select('#regularGroup_table > tr:nth-child(1) > td:nth-child(3)')

for t in tr:
    print(t.text)
