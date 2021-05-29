from bs4 import BeautifulSoup

f = open('playerList.html', 'r', encoding='utf-8')
soup = BeautifulSoup(f, 'html.parser')

trs = soup.select('tbody > tr')

for tr in trs:
    with open('playerList.txt', 'a', encoding='utf-8') as f:
        f.write(str(tr.get('onclick').replace('javascript:moveMainFrameMcPlayer', '').replace(';', '')) + '\n')
