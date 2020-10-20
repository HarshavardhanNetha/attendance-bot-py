from selenium import webdriver
from time import sleep
import getpass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#make sure codes have only subjects for which attendance is enabled
codes={"PS":'PS','AEC':'EC2105','DEC':'EC2101','HS':'HS2101',"DM":"CS2102"} #replace them with your Sub. codes. Make sure keys must be uppercase
flag=0

def login(user_id,pwd):
    driver.get("http://lms.rgukt.ac.in/login/index.php")
    sleep(0.5)
    driver.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys(user_id)
    driver.find_element_by_xpath("//input[@name=\"password\"]")\
        .send_keys(pwd)
    driver.find_element_by_xpath("//button[@type=\"submit\"]")\
        .click()
    sleep(2)

def moodle(sub_code):
    #simulate subject search and click
    sub_find = driver.find_elements_by_xpath("//span[contains(text(), '{}')]".format(sub_code))
    if(len(sub_find)!=0):
        sub_find[0].click()
        sleep(1)
    else:
        driver.find_element_by_xpath("//a[@title=\"{}\"]".format(sub_code)).click()
        sleep(1)
        
    driver.find_element_by_xpath("//span[contains(text(), 'Attendance')]").click()
    sleep(1)

    temp=0 #variable to check status

    #check whether it's correct time to submit attendance
    check_time=driver.find_elements_by_xpath("//a[contains(text(), 'Submit attendance')]")
    if(len(check_time)==0):
        global flag
        flag=1
        
    else:
        check_time[0].click()
        sleep(1)
        a=driver.find_element_by_xpath("//input[@name=\"status\"]").click()
        #a[0].click()

        b=driver.find_elements_by_xpath("//input[@type=\"submit\"]") 
        b[0].click()
        temp=1
        sleep(0.5)
    if(temp==0):
        print("Failed",sub_code)
    else:
        print("Success",sub_code)

user = "ID" #replace "ID" with your ID number
pwd = "Password" #replace "Password" with your password
<<<<<<< HEAD
=======
sub_code = "Subject Code" #replace "Subject Code" with code of subject that you see in dashborad for which you would like to submit attendance
>>>>>>> fcedde91db221463504b5052fd51ed737f02ea29

#remove below comments to make it interactive bot

#user = input("Enter your ID:")
#pwd = getpass.getpass(prompt="Enter your password:",stream=None)

<<<<<<< HEAD
choice=int(input("1. Automatic\t2. Manual:"))

if(choice==2):
    sub = input("Enter subject code to submit attendance:").upper()
    driver=webdriver.Chrome()
    login(user,pwd)
    sub_code=codes[sub]
    moodle(sub_code)
    if(flag==1):
        driver.execute_script("alert('Come back on correct time. Thank You!');")
        sleep(1)
        Keys.ENTER
        driver.quit()
    else:
        driver.execute_script("alert('Thank you for using. With ♡ @harsha :)');")
        sleep(2)
        driver.quit()

elif(choice==1):
    driver=webdriver.Chrome()
    login(user,pwd)
    for i in codes.keys():
        sub_code=codes[i]
        try:
            moodle(sub_code)
        except:
            driver.find_element_by_xpath("//span[contains(text(), 'Dashboard')]").click()
    driver.execute_script("alert('Thank you for using. With ♡ @harsha :)');")
    sleep(2)
    driver.quit()
=======
insta(user,pwd,sub_code)
>>>>>>> fcedde91db221463504b5052fd51ed737f02ea29
