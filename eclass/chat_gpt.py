from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import urllib.parse
import time

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

browser = webdriver.Chrome(options=options)
browser.get(url)

wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.NAME, "userDTO.userId")))

user_id = browser.find_element(By.NAME, "userDTO.userId")
browser.execute_script("arguments[0].value = '2019213014';", user_id)

user_pw = browser.find_element(By.NAME, "userDTO.password")
password_encoded = urllib.parse.quote("dusenal!@3")
browser.execute_script("arguments[0].value = 'dusenal!@3';", user_pw)
print(password_encoded)

# 로그인 버튼을 찾는 대기 시간을 10초로 설정
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'loginBtn')))
time.sleep(5)  # 5초 대기

# 로그인 버튼을 클릭
login_button = browser.find_element(By.CLASS_NAME, 'loginBtn')
login_button.click()

# 로그인 성공 후 나타나는 사용자 정보 요소를 대기
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'user-info')))

# 사용자 정보 요소가 존재하는지 확인하여 로그인 성공 여부 판단
if browser.find_elements(By.CLASS_NAME, 'user-info'):
    print("로그인 성공")
else:
    print("로그인 실패")

# 페이지 소스를 출력합니다.
print(browser.page_source)

# 브라우저를 종료합니다.
browser.quit()

