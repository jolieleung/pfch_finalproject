

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("/Users/jolieleung/Documents/GitHub/pfch_finalproject/chromedriver") 

from selenium.webdriver import ChromeOptions, Chrome
opts = ChromeOptions()
opts.add_experimental_option("detach", True)

#driver = webdriver.Chrome(options=opts, executable_path="./chromedriver")
driver = webdriver.Chrome(options=opts, service=s)

driver.get('https://www.google.com')




