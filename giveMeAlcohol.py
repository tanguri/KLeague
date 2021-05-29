from selenium.webdriver import Edge
from bs4 import BeautifulSoup

# Edge 드라이버 로딩
driver = Edge('driver/msedgedriver.exe')

# 숨겨진 K리그 데이터 포털
driver.get('https://portal.kleague.com/user/loginById.do?portalGuest=rstNE9zxjdkUC9kbUA08XQ==')

# 선수 정보 페이지
driver.execute_script('moveMainFrame("0410")')

playerList = open('playerList.txt', 'r', encoding='utf-8')

for p in playerList:
    print(p)
    driver.execute_script("moveMainFrameMcPlayer{}".format(p))
    driver.implicitly_wait(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    name = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(2)').string.strip()
    ename = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(1) > td:nth-child(4)').string.strip()
    club = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(2)').string.strip()
    position = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(2) > td:nth-child(4)').string.strip()
    back_no = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(2)').string.strip()
    nationality = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(4)').string.strip()
    height = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(4) > td:nth-child(2)').string.strip()
    weight = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(4) > td:nth-child(4)').string.strip()
    birthday = soup.select_one(
        '#searchForm > div > div > table:nth-child(1) > tbody > tr:nth-child(5) > td:nth-child(2)').string.strip()

    print(name, ename, club, position, back_no, nationality, height, weight, birthday)

    filename = (p.replace(',', '_').replace(' ', '').replace('(', '').replace(')', '').replace("'", "")).rstrip(
        '\n') + ".html"

    with open('player/{}'.format(filename), 'a', encoding='utf-8') as f:
        f.write(str(soup))

    # 뒤로가기 버튼
    driver.find_element_by_css_selector('#button-list').click()
    driver.implicitly_wait(3)
