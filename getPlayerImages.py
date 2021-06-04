# from selenium.webdriver import Edge
from bs4 import BeautifulSoup
import requests

#
# # Edge 드라이버 로딩
# driver = Edge('driver/msedgedriver.exe')
#
# # 숨겨진 K리그 데이터 포털
# driver.get('https://portal.kleague.com/user/loginById.do?portalGuest=rstNE9zxjdkUC9kbUA08XQ==')
#
# # 선수 정보 페이지
# driver.execute_script('moveMainFrame("0410")')
#
# soup = BeautifulSoup(driver.page_source, 'html.parser')
#
# with open('getPlayerImages.html', 'w', encoding='utf-8') as f:
#     f.write(str(soup))


f = open('getPlayerImages.html', 'r', encoding='utf-8')
soup = BeautifulSoup(f, 'html.parser')

tr = soup.select('#frm > table > tbody > tr')

for t in tr:
    p_id = t.attrs['onclick'].split(',')[1].replace("'", '')
    url = 'https://portal.kleague.com//common/playerPhotoById.do?playerId={}&recYn=Y&searchYear=2021'.format(p_id)
    print(url)

    response = requests.get(url)

    file = open("imgs/{}.png".format(p_id), "wb")
    file.write(response.content)
    file.close()
