from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

#user_id = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.NAME, "userDTO.userId")))

user_id = browser.find_element(By.NAME, "userDTO.userId")
#user_id.send_keys("2019213014")
browser.execute_script("arguments[0].value = '2019213014';", user_id)

user_pw = browser.find_element(By.NAME,"userDTO.password")
browser.execute_script("arguments[0].value = 'dusenal!@3';", user_pw)

login_button = browser.find_element(By.CLASS_NAME,'loginBtn')
browser.execute_script("arguments[0].click();", login_button)

print(browser.page_source)
