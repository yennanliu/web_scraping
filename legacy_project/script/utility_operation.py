from selenium import webdriver 

class Login():
	def user_login(self,driver):
		"""
		clear form before input id / password 
		can find element by other ways : Xpath/CSS/parent..
		"""
		# input user id 
		driver.find_element_by_id("idinput").clear()
		driver.find_element_by_id("idinput").send_keys("user_name")
		# iiput password 
		driver.find_element_by_id("pwdinput").clear()
		driver.find_element_by_id("pwdinput").send_keys("user_password")
		# click login button 
		driver.find_element_by_id("loginbtn").click()
		print ('### login success ###')
	def user_logout(self,driver):
		driver.find_element_by_link_text("logout").click()
		driver.quit()
		print ('### log out success ###')