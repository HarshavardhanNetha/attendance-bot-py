from selenium import webdriver
from time import sleep
import getpass

def insta(user_id,pwd,sub_code):
    driver=webdriver.Chrome()
    driver.get("http://lms.rgukt.ac.in/login/index.php")
    sleep(2)
    driver.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys(user_id)
    driver.find_element_by_xpath("//input[@name=\"password\"]")\
        .send_keys(pwd)
    driver.find_element_by_xpath("//button[@type=\"submit\"]")\
        .click()
    sleep(4)
    driver.find_element_by_xpath("//span[contains(text(), '{}')]".format(sub_code)).click()
    sleep(2)
    driver.find_element_by_xpath("//span[contains(text(), 'Attendance')]").click()
    sleep(2)
    
    check_time=driver.find_elements_by_xpath("//a[contains(text(), 'Submit attendance')]")
    if(len(check_time)==0):
        driver.execute_script("alert('Come back on correct time. Thank You!');")
        sleep(4)
    else:
        check_time[0].click()
        sleep(2)
        a=driver.find_element_by_xpath("//input[@name=\"status\"]").click()
        a[0].click()

        b=driver.find_elements_by_xpath("//input[@type=\"submit\"]") 
        b[0].click()
        sleep(2)
        driver.execute_script("alert('Thank you for using. With ♡ @harsha :)');")
        sleep(4)

user = "ID" #replace "ID" with your ID number
pwd = "Password" #replace "Password" with your password
sub_code = "Subject Code" #replace "Subject Code" with code of subject that you see in dashborad for which you would like to submit attendance

#remove below comments to make it interactive bot
#user = input("Enter your ID:")
#pwd = getpass.getpass(prompt="Enter your password:",stream=None)
#sub_code = input("Enter subject code to submit attendance:") #partialcode is also accepted Need to be unique

insta(user,pwd,sub_code)
