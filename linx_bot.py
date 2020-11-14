from selenium import webdriver
from time import sleep
import getpass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from datetime import date
from datetime import datetime

#make sure codes have only subjects for which attendance is enabled
codes={"PS":'PS','AEC':'EC2105','DEC':'EC2101','HS':'HS2101',"DM":"CS2102"} #replace them with your Sub. codes. Make sure keys must be uppercase
flag=0

driver_path = '/root/Downloads/geckodriver'

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
    f=open("logs_{}".format(date.today()),"a")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    f.write("{} \n".format(current_time))
    f.close()   

def moodle(sub_code):
    #simulate subject search and click
    sub_find = driver.find_elements_by_xpath("//span[contains(text(), '{}')]".format(sub_code))
    if(0): #unsued block
        sub_find[0].click()
        sleep(1)
    else:
        driver.find_element_by_xpath("//a[@title=\"{}\"]".format(sub_code)).click()
        sleep(1)
        
    driver.find_element_by_xpath("//span[contains(text(), 'Attendance')]").click()
    sleep(1)

    temp=0 #variable to check status
    f=open("logs_{}".format(date.today()),"a")


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
        #print("Failed",sub_code)
        f.write("Failed {} ".format(sub_code))
        
    else:
        #print("Success",sub_code)
        f.write("Success {} ".format(sub_code))
    f.write("\n")
    f.close()

user = "ID " #replace "ID" with your ID number
pwd = "Pwd" #replace "Password" with your password


#remove below comments to make it interactive bot

#user = input("Enter your ID:")
#pwd = getpass.getpass(prompt="Enter your password:",stream=None)

while(1):
	driver=webdriver.Firefox(executable_path = driver_path)
	login(user,pwd)
	for i in codes.keys():
		sub_code=codes[i]
		try:
		    moodle(sub_code)
		    driver.find_element_by_xpath("//a[contains(text(), 'Dashboard')]").click()
		except:
		    pass
	driver.execute_script("alert('Thank you for using. @harsha :)');")
	sleep(2)
	driver.quit()
	sleep(60*60)
