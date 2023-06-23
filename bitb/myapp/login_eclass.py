from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def isLogin(isTrue):
    return isTrue != -1

def eclass_confirm(sc_number, sc_pw):
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

    with webdriver.Chrome(options=options) as browser:
        wait = WebDriverWait(browser, 10)

        browser.get(url)
        wait.until(EC.presence_of_element_located((By.NAME, "userDTO.userId")))

        user_id = browser.find_element(By.NAME, "userDTO.userId")
        browser.execute_script(f"arguments[0].value = '{sc_number}';", user_id)

        user_pw = browser.find_element(By.NAME, "userDTO.password")
        browser.execute_script(f"arguments[0].value = '{sc_pw}';", user_pw)

        login_button = browser.find_element(By.CLASS_NAME, 'loginBtn')
        browser.execute_script("arguments[0].click();", login_button)

        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
            boolean = "로그아웃" in browser.page_source
            print("login succeeded")
        except UnexpectedAlertPresentException as e:
            print("에러 메시지:", e.msg)
            # 예외 처리를 원하는 대로 수행하세요.
            # 예를 들어, 로그인 실패를 처리하는 로직을 추가할 수 있습니다.
            boolean = False
            print("failed login")
    print(boolean)
    return boolean

# 테스트
#sc_num = input("sc_number: ")
#sc_pwd = input("sc_pw: ")
#result = eclass_confirm(sc_num, sc_pwd)
#print("로그인 성공:", result)

