from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
#Get webdriver
s=Service('/Users/carsongodwin/Desktop/Webscraper/chromedriver')
driver = webdriver.Chrome(service=s)
#Set URl
url = 'https://www.google.com/search?q=bowling&rlz=1C5CHFA_enUS922US923&oq=bowling&aqs=chrome.0.69i59j35i39j0i131i433i457i512j0i402j0i131i433i512j46i433i512j0i131i433i512l2j0i512j46i433i512.1120j0j4&sourceid=chrome&ie=UTF-8'
driver.get('https://www.google.com/search?q=bowling&rlz=1C5CHFA_enUS922US923&oq=bowling&aqs=chrome.0.69i59j35i39j0i131i433i457i512j0i402j0i131i433i512j46i433i512j0i131i433i512l2j0i512j46i433i512.1120j0j4&sourceid=chrome&ie=UTF-8')

elements = driver.find_elements(By.CSS_SELECTOR, 'h3')
search_results = []
for i in range(20):
    search_results.append(elements[i].text)
    time.sleep(.05)
print(search_results)

driver.close()