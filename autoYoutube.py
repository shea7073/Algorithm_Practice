from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = '/Users/seanshea/chromedriver'

driver = webdriver.Chrome(PATH)

#driver.get("https://google.com")

#search = driver.find_element_by_name("q")

driver.get("https://youtube.com")

search = driver.find_element_by_name("search_query")

search.send_keys("Laymen Gaming")

search.send_keys(Keys.RETURN)

