

from selenium import webdriver

from selenium.webdriver import ChromeOptions, Chrome
opts = ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=opts, executable_path=r"C:\Users\leung\Downloads\chromedriver_win32\chromedriver.exe")

driver.get('https://www.google.com')

