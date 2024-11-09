from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#set chromodriver.exe path and actions
driver = webdriver.Chrome()

#Go to webaddress
driver.get("http://localhost/ecommerce_tutorial/login.html")

#Login with Username and Password
username = driver.find_element(By.ID, "username")
username.send_keys("Lu")
password = driver.find_element(By.ID, "password")
password.send_keys("happy")

#Login and wait some time
password.send_keys(Keys.ENTER)
time.sleep(1)

#Click Ok and wait
WebDriverWait(driver,5).until(EC.alert_is_present())
driver.switch_to.alert.accept()
time.sleep(3)

#Add Bags to Cart
BagQ=driver.find_element(By.ID, "product1_quantity").send_keys("0")
time.sleep(1)
BagCart=driver.find_element(By.NAME, "add_to_cart").send_keys(Keys.ENTER)
time.sleep(10)

#Go back to Shop Page
Shop=driver.find_element(By.LINK_TEXT, 'Home').send_keys(Keys.ENTER)
time.sleep(2)

#Add shirts to cart
ShirtQ=driver.find_element(By.ID, "product2_quantity" )
ShirtQ.send_keys('2')
time.sleep(1)
ShirtQ.send_keys(Keys.ENTER)
time.sleep(1)

#Go back to Shop Page
Shop=driver.find_element(By.LINK_TEXT, 'Home').send_keys(Keys.ENTER)
time.sleep(2)

#Add Hoodies to Cart
HoodiesQ=driver.find_element(By.ID, "product3_quantity")
HoodiesQ.send_keys('4')
time.sleep(1)
HoodiesQ.send_keys(Keys.ENTER)
time.sleep(1)

#Go back to Shop Page
Shop=driver.find_element(By.LINK_TEXT, 'Home').send_keys(Keys.ENTER)
time.sleep(1)

#ViewCart
Cart=driver.find_element(By.LINK_TEXT, 'Cart').send_keys(Keys.ENTER)
time.sleep(1)


time.sleep(30)

