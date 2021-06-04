# https://sports.news.naver.com/kfootball/record/index.nhn?category=kleague&year=2021

from bs4 import BeautifulSoup
import requests

url = 'https://sports.news.naver.com/kfootball/record/index.nhn?category=kleague&year=2021'

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

td = soup.select('#regularGroup_table > tr > td')
rank = soup.select('#regularGroup_table > tr > th > strong')
team_name = soup.select('#regularGroup_table > tr > td.tm > div > span')
played = soup.select('#regularGroup_table > tr > td:nth-child(3)')
points = soup.select('#regularGroup_table > tr > td:nth-child(4) > strong')
won = soup.select('#regularGroup_table > tr > td:nth-child(5)')
drown = soup.select('#regularGroup_table > tr > td:nth-child(6)')
lost = soup.select('#regularGroup_table > tr > td:nth-child(7)')
gf = soup.select('#regularGroup_table > tr > td:nth-child(8)')
ga = soup.select('#regularGroup_table > tr > td:nth-child(9)')
gd = soup.select('#regularGroup_table > tr > td:nth-child(10)')
assist = soup.select('#regularGroup_table > tr > td:nth-child(11)')
fo = soup.select('#regularGroup_table > tr > td:nth-child(12)')

