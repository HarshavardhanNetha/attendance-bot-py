from selenium import webdriver
from flask import Flask
from selenium.webdriver.firefox.options import Options
from datetime import date
from datetime import datetime
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

app=Flask(__name__)

@app.route('/')
def hello():
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
		f=open("logs_{}".format(date.today()),"a")
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		f.write("{} \n".format(current_time))
		f.close()
		
	def moodle(sub_code):
	
		#simulate subject search and click
		status=''
		sub_find = driver.find_elements_by_xpath("//span[contains(text(), '{}')]".format(sub_code))
		if(0): #unsued block
		    sub_find[0].click()
		    sleep(1)
		else:
		    #driver.find_element_by_xpath("//a[@title=\"{}\"]".format(sub_code)).click()
		    #sleep(1)
		    element = driver.find_element_by_xpath("//a[@title=\"{}\"]".format(sub_code))
		    #driver.execute_script("arguments[0].click();", element)
		    #ActionChains(driver).move_to_element(element).click().perform()
		    driver.execute_script("window.scrollBy(0,100)")
		    element.click()
		    
		ele_sub=driver.find_element_by_xpath("//span[contains(text(), 'Attendance')]")
		driver.execute_script("window.scrollBy(0,100)")
		ele_sub.click()
		sleep(1)

		temp=0 #variable to check status
		f=open("logs_{}".format(date.today()),"a")


		#check whether it's correct time to submit attendance
		check_time=driver.find_elements_by_xpath("//a[contains(text(), 'Submit attendance')]")
		if(len(check_time)==0):
		    global flag
		    flag=1
		    
		else:
		    driver.execute_script("window.scrollBy(0,100)")
		    check_time[0].click()
		    sleep(1)
		    a=driver.find_element_by_xpath("//input[@name=\"status\"]").click()
		    #a[0].click()

		    b=driver.find_elements_by_xpath("//input[@type=\"submit\"]") 
		    b[0].click()
		    temp=1
		    sleep(0.5)
		if(temp==0):
		    res="Failed {} ".format(sub_code)
		    f.write(res)
		    print(res)
		    
		    
		else:
		    res="Success {} ".format(sub_code)
		    f.write(res)
		    print(res)
		    
		f.write("\n")
		f.close()

	user = "ID" #replace "ID" with your ID number
	pwd = "pwd" #replace "Password" with your password

	options = Options()
	driver_path = '/root/Desktop/moodle-docker/geckodriver'
	options.headless = True
	driver=webdriver.Firefox(executable_path = driver_path,options=options)
	print("driver started.")
	try:
		login(user,pwd)
		print("Login successful")
	except:
		f=open("logs_{}".format(date.today()),"a")
		now = datetime.now()
		current_time = now.strftime("%H:%M:%S")
		f.write("{} - Login Unsuccessful \n".format(current_time))
		f.close()   
		sleep(0.5)
		driver.quit()
		print("Login Failed: Server Error")
		return "Login Failed Server error."
		exit(0)
	for i in codes.keys():
		sub_code=codes[i]
		try:
			moodle(sub_code)
			driver.find_element_by_xpath("//a[contains(text(), 'Dashboard')]").click()
		except:
			pass
	driver.quit()
	return "Successful "

if __name__ == '__main__':
	app.run(debug=True)
