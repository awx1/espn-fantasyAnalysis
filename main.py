import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request as urllib2

driver = webdriver.Chrome()

driver.get("http://espn.com/login")
#implement wait it is mandatory in this case

time.sleep(10)
driver.find_element_by_xpath('/html/body/div/div/div/section/section/form/section/div[1]/div/label/span[2]/input').send_keys("alexanderx2008@gmail.com")
driver.find_element_by_xpath('//*[@id="did-ui-view"]/div/section/section/form/section/div[2]/div/label/span[2]/input').send_keys("password")

driver.find_element_by_xpath('//*[@id="did-ui-view"]/div/section/section/form/section/div[3]/button').click()
driver.switch_to_default_content()


