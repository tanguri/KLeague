from bs4 import BeautifulSoup
import requests

players = ''

for year in range(2021, 2022):
    url = 'https://www.kleague.com/record/return_history_html?select_history_type=club_player&datatype=html&select_league_year={}&select_league={}&select_club=K{}&del_target=tbody%23club_player_list%20tr&add_target=tbody'.format(
        year, '1', '05')

    r = requests.get(url)

    soup = BeautifulSoup(r.content, 'html.parser')

    players = soup.select('tr')


pp = players[0].text

player = pp.split('\n')

print(player)

team = [1,2,3,4,5]

for i in team:

    print(i)