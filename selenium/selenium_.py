# import time
# from selenium import webdriver

# driver = webdriver.Chrome('WebScraping/selenium/chromedriver.exe')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/')
# time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()


from selenium import webdriver
import time
from selenium.webdriver.common.by import By

website = 'https://www.adamchoi.co.uk/overs/detailed'
# path = 'chromedriver.exe'
driver = webdriver.Chrome()
driver.get(website)
time.sleep(5)
all_matches_button = driver.find_elements(By.XPATH,'//label[@analytics-event="All matches"]')
all_matches_button[0].click()
time.sleep(5)

matches = driver.find_elements(By.TAG_NAME, 'tr')
for match in matches:
    print(match.text)

time.sleep(5)
driver.quit()