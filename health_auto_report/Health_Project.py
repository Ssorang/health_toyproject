from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from requests import get

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import pyautogui

browser_path = "https://gbehcm.eduro.go.kr/"

id = "eksajrm0624"
pw = "Dltkdals1!"

# 맥 환경에서 복사 -> 붙여넣기
def paste():
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')

# 백그라운드에서 다운로드 기능 활성화
def enable_download(driver):
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': '/Users/sorang/Downloads'}}
    driver.execute("send_command", params)    

def setting_chrome_options():
    print('옵션 설정')
    options = webdriver.ChromeOptions()
    options.add_argument('headless') # 백그라운드 작업
    return options

# 브라우저 꺼짐
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])

# 백그라운드 실행 옵션
chrome_options.add_argument("headless")

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동 로그인 페이지
driver.implicitly_wait(5) # 웹페이지가 로딩될 때까지 5초는 기다림
driver.maximize_window() # 화면 최대화
driver.get(browser_path)

# 백그라운드에서 다운로드 기능 활성화
enable_download(driver)

def Login():
    # 아이디 입력창
    driver.find_element(By.CSS_SELECTOR, "#lusername").send_keys(id)

    # 비밀번호 입력창
    driver.find_element(By.CSS_SELECTOR, "#lpassword").send_keys(pw) # 태그 자동으로 선택

    # 로그인 버튼
    login_btn = driver.find_element(By.CSS_SELECTOR, "body > div > div.login > form > div > button").click()

    Download()

######### 사이트 접속 이후 #########

def Download():
    Today_Participation_btn = driver.find_element(By.CSS_SELECTOR, "#lnb > li:nth-child(1) > a").click()

    Search_btn = driver.find_element(By.CSS_SELECTOR, "#searchForm > ul > li.group.group2 > input").click()

    driver.find_element(By.CSS_SELECTOR, "#searchButton > ul > li:nth-child(2) > ul > li > button").click()
    download = Alert(driver)
    download.accept() 

Login()

quit()