from selenium import webdriver
from flask import Flask
from selenium.webdriver.firefox.options import Options
from datetime import date
from datetime import datetime
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
app=Flask(__name__)

@app.route('/')
def hello():
	codes={"PS":'PS','AEC':'EC2105','DEC':'EC2101','HS':'HS2101'} #replace them with your Sub. codes. Make sure keys must be uppercase
	#print("Started")
	
	def login(user_id,pwd):
		login_che=1
		driver.set_page_load_timeout(15)
		try:
			driver.get("http://lms.rgukt.ac.in/login/index.php")
		except TimeoutException as e:
			#print("Page load Timeout Occured. Quiting !!!")
			login_che=2
			return login_che
    		
		#sleep(0.5)
		driver.find_element_by_xpath("//input[@name=\"username\"]")\
		    .send_keys(user_id)
		driver.find_element_by_xpath("//input[@name=\"password\"]")\
		    .send_keys(pwd)
		driver.find_element_by_xpath("//button[@type=\"submit\"]")\
		    .click()
		#sleep(0.5)
		
		
		if(driver.title=='Dashboard'):
			pass
		else:
			login_che=0
			
		return login_che
			
		
	def moodle(sub_code):
	
		#simulate subject search and click
		element = driver.find_element_by_xpath("//a[@title=\"{}\"]".format(sub_code))
		    #driver.execute_script("arguments[0].click();", element)
		    #ActionChains(driver).move_to_element(element).click().perform()
		driver.execute_script("window.scrollBy(0,100)")
		element.click()
		    
		ele_sub=driver.find_element_by_xpath("//span[contains(text(), 'Attendance')]")
		driver.execute_script("window.scrollBy(0,100)")
		ele_sub.click()
		sleep(0.2)

		temp=0 #variable to check status
		f=open("logs_{}".format(date.today()),"a")


		#check whether it's correct time to submit attendance
		check_time=driver.find_elements_by_xpath("//a[contains(text(), 'Submit attendance')]")
		if(len(check_time)==0):
			pass    
		else:
		    driver.execute_script("window.scrollBy(0,100)")
		    check_time[0].click()
		    sleep(0.5)
		    a=driver.find_element_by_xpath("//input[@name=\"status\"]").click()
		    #a[0].click()

		    b=driver.find_elements_by_xpath("//input[@type=\"submit\"]") 
		    b[0].click()
		    temp=1
		    sleep(0.5)
		if(temp==0):
		    res="Failed {} ".format(sub_code)
		    #f.write(res)
		    #print(res)
		    
		    
		else:
		    res="Success {} ".format(sub_code)
		    f.write(res)
		    #print(res)
		    
		f.write("\n")
		f.close()
		return res

	user = "ID" #replace "ID" with your ID number
	pwd = "Password" #replace "Password" with your password

	options = Options()
	driver_path = './geckodriver'
	options.headless = True
	driver=webdriver.Firefox(executable_path = driver_path,options=options)
	#print("driver started.")
	
	

	f=open("logs_{}".format(date.today()),"a")
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print("Start {}".format(current_time))
	login_status=login(user,pwd)

	if(login_status==1):
		#print("Login successful")
		f.write("{} {} Logged In\n".format(current_time,user))
		pass
	elif(login_status==2): #server Error
		driver.quit()
		f.write("{} {} Server Error\n".format(current_time,user))
		return "Server Error"
	else:
		f.write("{} {} Error - ID/Password Mismatch \n".format(current_time,user))
		f.close()
		sleep(0.5)
		driver.quit()
		return "Login Id/Password Error."
	
	ending_note=''
	for i in codes.keys():
		sub_code=codes[i]
		try:
			ending_note+=moodle(sub_code)
			driver.find_element_by_xpath("//a[contains(text(), 'Dashboard')]").click()
		except:
			pass
	driver.quit()

	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")


	print("Done {}".format(current_time))
	return "Login Successful {}".format(ending_note)

if __name__ == '__main__':
	app.run(host="0.0.0.0",debug=True)
	#serve(app,host="localhost",port="5000")
