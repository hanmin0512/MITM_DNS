from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
# 크롬 드라이버 경로 설정
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

url = "https://eclass.dongguk.ac.kr/Main.do?cmd=viewHome"

driver = webdriver.Chrome(options=options)
driver.get(url)

wait = WebDriverWait(driver, 10)
user_id = wait.until(EC.presence_of_element_located((By.ID, 'id')))
user_id.send_keys('2019213014')
# 아이디 입력
#user_id.clear()
#user_id.send_keys('2019213014')

# 비밀번호 입력 필드 찾기
password = driver.find_element(By.ID, 'pw')

# 비밀번호 입력
password.clear()
password.send_keys('dusenal!@3')

# 로그인 버튼 클릭
login_button = driver.find_element(By.CSS_SELECTOR, 'a.loginBtn')
login_button.click()

# 로그인 후 필요한 작업 수행
# ...
print(driver.page_source)

# 드라이버 종료
driver.quit()

