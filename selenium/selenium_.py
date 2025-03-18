

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

website = 'https://www.adamchoi.co.uk/overs/detailed'
# path = 'chromedriver.exe'
driver = webdriver.Chrome()
driver.get(website)
time.sleep(5)
all_matches_button = driver.find_element(By.XPATH,'//label[@analytics-event="All matches"]')
all_matches_button.click()
time.sleep(2)

matches = driver.find_elements(By.TAG_NAME, 'tr')
# for match in matches:
#     print(match.text)

date = []
home_team = []
score = []
away_team = []

for match in matches:
    date.append(match.find_element(By.XPATH, './td[1]').text)
    home_team.append(match.find_element(By.XPATH, './td[3]').text)
    score.append(match.find_element(By.XPATH, './td[4]').text)
    away_team.append(match.find_element(By.XPATH, './td[5]').text)

df = pd.DataFrame({'Date': date, 'Home Team': home_team, 'Score': score, 'Away Team': away_team})
df.to_csv('matches.csv', index=False)

# time.sleep(5)
driver.quit()