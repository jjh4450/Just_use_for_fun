from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

def main():

    print('run')

    driver = webdriver.Chrome('<driver>')
    driver.get('https://hcs.eduro.go.kr/#/loginHome')
    time.sleep(1)

    def Fid(val):
        tag_school = driver.find_element_by_id(val)
        tag_school.click()

    def sidolabel(val):
        tag_city = driver.find_element_by_xpath("//option[@value ='" + str(val) + "']")
        tag_city.click()

    def Fxpath(val):
        tag_xpath = driver.find_element_by_xpath(val)
        tag_xpath.click()

    def input_by_id(val, data):
        pyperclip.copy(data)
        tag_id = driver.find_element_by_id(val)
        tag_id.click()
        tag_id.send_keys(Keys.CONTROL, 'v')

    def input_by_xpath(val, data):
        pyperclip.copy(data)
        tag_xpath = driver.find_element_by_xpath(val)
        tag_xpath.click()
        tag_xpath.send_keys(Keys.CONTROL, 'v')

    time.sleep(1)

    # go 버튼 클릭

    butt_go = driver.find_element_by_id('btnConfirm2')
    butt_go.click()

    # 학교찾기를 들어감
    Fid('schul_name_input')

    # 학교찾기-시도
    Fid('sidolabel')
    sidolabel('<City/Province>')
    ''' 
        <City/Province>
        서울:01
        부산:02
        대구:03
        인천:04
        광주:05
        대전:06
        울산:07
        세종:08
        경기:10
        강원:11
        충북:12
        충남:13
        전북:14
        전남:15
        경북:16
        경남:17
        제주:18
    '''

    # 학교찾기-학교급
    Fid('crseScCode')
    sidolabel('<school_level>')

    ''' 
        <school_level>
        유치원:1
        초등학교: 2
        중학교: 3
        고등학교: 4
        특수학교등: 5
    '''

    # 학교 검색-키워드
    input_by_id('orgname', '<school_name>')
    time.sleep(1)

    # 학교 검색-검색
    Fxpath("/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/button")
    time.sleep(1)

    # 학교 검색-학교선택
    Fxpath("/html/body/div/div/div/div/div/div[2]/div[1]/ul/li/a/p/a")
    time.sleep(1)

    Fxpath("/html/body/div/div/div/div/div/div[2]/div[2]/input")
    time.sleep(1)

    # 성명 입력
    input_by_id('user_name_input', '<name>')
    time.sleep(1)

    # 생년월일 입력
    input_by_id('birthday_input', '<birthday>')
    time.sleep(1)

    # 확인 누름
    Fid('btnConfirm')
    time.sleep(2)  # 정보 확인에 시간 조금걸림

    # pw 입력
    input_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/div[1]/table/tbody/tr/td/input', '<pw>')
    time.sleep(1)

    # 확인 누름
    Fid('btnConfirm')
    time.sleep(2)  # 정보 확인에 시간 조금걸림

    # 참여자 목록 에서 내꺼 클릭하기
    tag_me = driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/section[2]/div[2]/ul/li/a/span[1]')
    tag_me.click()
    time.sleep(2)

    # 응답 ㄱ

    Fid('survey_q1a1')
    time.sleep(1)
    Fid('survey_q2a1')
    time.sleep(1)
    Fid('survey_q3a1')
    time.sleep(1)
    #survey_q(문항 숫자)a(1:아니요 2:예)
    
    # 확인 누름
    Fid('btnConfirm')
