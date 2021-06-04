from selenium.webdriver import Edge
from bs4 import BeautifulSoup

# Edge 드라이버 로딩
driver = Edge('driver/msedgedriver.exe')

# 숨겨진 K리그 데이터 포털
driver.get('https://portal.kleague.com/user/loginById.do?portalGuest=rstNE9zxjdkUC9kbUA08XQ==')

# 선수 정보 페이지
driver.execute_script('moveMainFrame("0058")')
driver.implicitly_wait(1)

driver.find_element_by_xpath('//*[@id="scoreBtn_18"]').click()
driver.implicitly_wait(1)

driver.get('https://portal.kleague.com/common/result/resultdataPopup0058.do')

soup = BeautifulSoup(driver.page_source, 'html.parser')

print(soup)