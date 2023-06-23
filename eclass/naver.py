from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

url = "https://eclass.dongguk.ac.kr/"

browser = webdriver.Chrome(options=options)
browser.get(url)
user_id = browser.find_element(By.ID, 'id')
user_id.send_keys('2019213014')

# 비밀번호 입력
password = browser.find_element(By.ID, 'pw')
password.send_keys('dusenal!@3')
login_button = driver.find_element(By.CLASS_NAME, 'loginBtn')
login_button.click()
driver.implicitly_wait(10)
print(browser.page_source)
driver.quit()
