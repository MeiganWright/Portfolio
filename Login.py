from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#set chromodriver.exe path
driver = webdriver.Chrome()

#launch URL
driver.get("http://localhost/ecommerce_tutorial/login.html")


username = driver.find_element(By.ID, "username")
username.send_keys("Lulu")

password = driver.find_element(By.ID, "password")
password.send_keys("happy")

#login=driver.find_element(By.TYPE, "submit")
password.send_keys(Keys.ENTER)
time.sleep(15)


driver.quit()