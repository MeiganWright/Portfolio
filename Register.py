from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#set chromodriver.exe path
driver = webdriver.Chrome()

#launch URL
driver.get("http://localhost/ecommerce_tutorial/login.html")
time.sleep(3)
register=driver.find_element(By.LINK_TEXT, 'Click Here')
register.click()
time.sleep(1)

name=driver.find_element(By.ID, "name")
name.send_keys("Lu")
time.sleep(1)

newusername=driver.find_element(By.ID, "username")
newusername.send_keys("Lu")
time.sleep(1)

email=driver.find_element(By.ID, "email")
email.send_keys("Lu@email.com")
time.sleep(1)

newpassword=driver.find_element(By.ID,"password")
newpassword.send_keys("happy")
time.sleep(3)

newpassword.send_keys(Keys.ENTER)

time.sleep(30)