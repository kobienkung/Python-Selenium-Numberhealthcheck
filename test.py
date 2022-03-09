from selenium import webdriver
import csv
from selenium.webdriver.common.keys import Keys # assuming using keybaord
import time
import  datetime

driver_path = r"C:\Users\kobienkung\OneDrive - KMITL\PROGRAM\chromedriver.exe"

url = 'https://dtaconline.dtac.co.th/newnumber/numberhealthcheck/'

'''
class AA:
    def __init__(self, driver=webdriver.Chrome(driver_path)):
        self.driver = driver
    
    def land(self):
        self.driver.get(url)
'''

driver = webdriver.Chrome(driver_path)
driver.get(url)
driver.implicitly_wait(8)
driver.maximize_window()

calendar = driver.find_element_by_id('dob-picker')
calendar.click()
yearCalendar = driver.find_element_by_class_name('yearselect')
yearCalendar.click()
yearSelect = driver.find_element_by_css_selector(
    'option[value="1998"]'
    #'option[value="1997"]'
)
yearSelect.click()

monthCalendar = driver.find_element_by_class_name('monthselect')
monthCalendar.click()
monthSelect = driver.find_element_by_css_selector(
    'option[value="2"]'
    #'option[value="3"]'
)
monthSelect.click()

dateSelect = driver.find_element_by_css_selector(
    'td[data-title="r2c4"]'
    #'td[data-title="r2c5"]'
)
dateSelect.click()


def last4number(*num):
    numLength = len(num)
    numNum = '0'
    for i,v in enumerate(range(2,11)):
        a = driver.find_element_by_id('number_pos' + str(v))
        if 10 - v >= numLength:
            a.send_keys(0)
            numNum += '0'
        else: 
            a.send_keys(num[i-5])
            numNum += str(num[i-5])
    return numNum

#last4number(9,8,7,6)
#last4number(8,6,9,5)


def check():
    time.sleep(2)
    checkSelect = driver.find_element_by_css_selector(
        'button[class="btn-check-number primary"]'
    )
    checkSelect.click()

def attribute():
    try:
        att = driver.find_element_by_css_selector('div[class="box-nice-number"]')
        subAtt = att.find_elements_by_css_selector('*')
        luck = ['ตำแหน่งก้าวไกล ผู้ใหญ่อุปถัมภ์','ส่งเสริมธุรกิจ พิชิตทุกการค้าขาย','เจรจาง่าย โน้มน้าวใจสำเร็จ','ร่ำรวย ปลดหนี้ มั่งมีมั่งคั่ง','ลงทุนรับทรัพย์ ลาภหล่นทับรับโชค','เสริมเสน่ห์ ได้เจอเนื้อคู่','ให้รักกันดี มีแต่หวานชื่น']
        length = len(luck)
        for sub in subAtt:
            fortune = []
            a = str(sub.get_attribute('innerHTML')).strip()
            for ind in range(length):
                if luck[ind] in a :
                    fortune.append(1)
                else:
                    fortune.append(0)
            return fortune
    except:
        return []

def grade():
    time.sleep(2)
    try:
        Grade = driver.find_element_by_css_selector('div[class="points"]')
        subGrade = Grade.find_element_by_class_name('left-box').find_elements_by_css_selector('*')
        Grades = ['A+','A','B','C','D','F']
        for sub in subGrade:
            a = str(sub.get_attribute('innerHTML')).strip()
            if a in Grades:
                return a
    except:
        return '?'

def loveStar():
    try:
        rightBox = driver.find_element_by_class_name('right-box')
        love = rightBox.find_element_by_css_selector('div[class="ratings clearfix love"]')
        HTMLtext = str(love.get_attribute('innerHTML'))
        return HTMLtext.count('star-ico active')
    except:
        return '?'

def financeStar():
    try:
        rightBox = driver.find_element_by_class_name('right-box')
        love = rightBox.find_element_by_css_selector('div[class="ratings clearfix finance"]')
        HTMLtext = str(love.get_attribute('innerHTML'))
        return HTMLtext.count('star-ico active')
    except:
        return '?'

def workStar():
    try:
        rightBox = driver.find_element_by_class_name('right-box')
        love = rightBox.find_element_by_css_selector('div[class="ratings clearfix work"]')
        HTMLtext = str(love.get_attribute('innerHTML'))
        return HTMLtext.count('star-ico active')
    except:
        return '?'



start_time = datetime.datetime.today()
print(start_time)
with open('HealthyNumber1.csv', 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile, delimiter=',')
    head = ['Number', 'Grade', 'workStar', 'financeStar', 'loveStar', 'w1', 'w2', 'w3', 'f1', 'f2', 'l1', 'l2']
    writer.writerow(head)
    start = 5752
    for a in range(0,10):
        for b in range(0,10):
            for c in range(0,10):
                for d in range(0,10):
                    if int(str(a)+str(b)+str(c)+str(d)) < start:
                        continue
                    fate = []
                    fate.append(last4number(a,b,c,d))
                    try:
                        check()
                    except:
                        print('---------------- RUN TIME = ', datetime.datetime.today()-start_time ,'----------------')
                        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'r')
                        time.sleep(5)
                        check()
                    fate.append(grade())
                    fate.append(loveStar())
                    fate.append(workStar())
                    fate.append(financeStar())
                    for x in attribute():
                        fate.append(x)
                    writer.writerow(fate)
                    if int(str(a)+str(b)+str(c)+str(d)) >= 4177+1940:
                        driver.quit()
                        break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    driver.quit()
