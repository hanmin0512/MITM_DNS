from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import urllib.parse

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

wait = WebDriverWait(browser, 140)
wait.until(EC.presence_of_element_located((By.NAME, "userDTO.userId")))

user_id = browser.find_element(By.NAME, "userDTO.userId")
browser.execute_script("arguments[0].value = '2019213014';", user_id)

user_pw = browser.find_element(By.NAME, "userDTO.password")
password_encoded = urllib.parse.quote("dusenal!@3")
browser.execute_script("arguments[0].value = 'dusenal!@3';", user_pw)
print(password_encoded)


login_button = browser.find_element(By.CLASS_NAME, 'loginBtn')
browser.execute_script("arguments[0].click();", login_button)

# 대기 시간을 조정하여 페이지가 로드될 때까지 기다립니다.
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))

# 페이지 소스를 출력합니다.
print(browser.page_source)


'''
# 로그인 성공 여부를 확인하기 위해 페이지 URL을 가져옵니다.
#current_url = browser.current_url

# 세션을 유지하는 requests 객체를 생성합니다.
session = requests.Session()

# 리디렉션된 URL로 GET 요청을 보냅니다.
response = session.get(current_url)

# 응답 헤더를 가져옵니다.
response_headers = response.headers
print(response_headers)

# 로그인 성공 여부를 확인합니다.
if response_headers.get("Location") == "https://eclass.dongguk.ac.kr/Main.do?cmd=viewHome":
    print("로그인 성공")
else:
    print("로그인 실패")
    print(response_headers)
# 브라우저를 종료합니다.
'''
browser.quit()

