from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from requests import get

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time
import pyautogui
import pyperclip
import openpyxl
import requests

browser_path = "https://gbehcm.eduro.go.kr/"

def paste():
    pyautogui.keyDown('command')
    pyautogui.press('v')
    pyautogui.keyUp('command')

# 브라우저 꺼짐
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ['enable-logging'])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이동 로그인 페이지
driver.implicitly_wait(5) # 웹페이지가 로딩될 때까지 5초는 기다림
driver.maximize_window() # 화면 최대화
driver.get(browser_path)

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#lusername") # 태그 자동으로 선택
id.click()
pyperclip.copy("eksajrm0624")
paste()
time.sleep(1)

# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#lpassword") # 태그 자동으로 선택
pw.click()
pyperclip.copy("Dltkdals1!")
paste()
time.sleep(1)

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "body > div > div.login > form > div > button")
login_btn.click()
time.sleep(1)


######### 사이트 접속 이후 #########

Today_Participation_btn = driver.find_element(By.CSS_SELECTOR, "#lnb > li:nth-child(1) > a")
Today_Participation_btn.click()
time.sleep(1)

Search_btn = driver.find_element(By.CSS_SELECTOR, "#searchForm > ul > li.group.group2 > input")
Search_btn.click()

# 데이터 집계
response = get(current_url = driver.current_url)
print(response)
if response.status_code != 200 :
    print("Can`t request website")
else :
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.find_all("p"))




