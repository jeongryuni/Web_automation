# Selenium : 브라우저를 자동화하는 도구
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_experimental_option("detach", True)

# 크롬 드라이버 생성
driver = webdriver.Chrome(options=options)
# driver.implicitly_wait(3) # 페이지 로딩을 기다리기 위한 초
wait = WebDriverWait(driver,3)

# 사이트 접속하기
driver.get('https://workey.codeit.kr/costagram/index')

# 로그인 버튼 클릭
login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.top-nav__login-link')))
login_link.click()

# 아이디 입력
id_box = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__login-input')))
id_box.send_keys('codeit')
driver.find_element(By.CSS_SELECTOR, '.login-container__password-input').send_keys('datascience') # 비밀번호 입력
driver.find_element(By.CSS_SELECTOR, '.login-container__login-button').click()
sleep(5)

'''
element_to_be_clickable(): 웹 요소가 클릭 가능한 상태일 때까지 기다림.
visibility_of_element_located(): 웹 요소가 실제로 보일 때까지 기다림.
text_to_be_present_in_element(): 웹 요소 안에 텍스트가 로딩될 때까지 기다림.
invisibility_of_element_located(): 웹 요소가 안 보일 때까지 기다림.
'''
# 크롬 드라이버 종료
# driver.quit()

# Wait 설정하기
'''
implicit wait : 웹 드라이버에 implicit wait을 설정해 주면 찾으려고 하는 웹 요소가 없을 때, 최대 설정해 준 기간만큼 기다려 줍니다.
sleep() : time 모듈의 sleep()은 정해진 기간만큼 동작을 멈춥니다.
'''