
import glob

all_existing_html_files = list(glob.glob('/Users/jolieleung/Documents/GitHub/pfch_finalproject/html/*.html'))
#print(all_existing_html_files)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
s = Service("/Users/jolieleung/Documents/GitHub/pfch_finalproject/chromedriver") 

from selenium.webdriver import ChromeOptions, Chrome
opts = ChromeOptions()
opts.add_experimental_option("detach", True)

#driver = webdriver.Chrome(options=opts, executable_path="./chromedriver")
driver = webdriver.Chrome(options=opts, service=s)

driver.get('https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderProfileResults.aspx')

js_command = """

    document.getElementById('MainContentPlaceHolder_pagingUserControlTop_RecordsPerPage').value = 24;
    document.getElementById('MainContentPlaceHolder_pagingUserControlTop_RecordsPerPage').dispatchEvent( new Event('change') );

"""


driver.execute_script(js_command)


for page in range(1,357):

    filename = f'html/source_{page}.html'

    if filename in all_existing_html_files:
        print('Skipping page:',page)
        continue

    print('Doing page',page)

    js_command_page = f"""
		document.getElementById('MainContentPlaceHolder_pagingUserControlTop_pageTextBox').value = {page};
		document.getElementById('MainContentPlaceHolder_pagingUserControlTop_pageTextBox').dispatchEvent( new KeyboardEvent('keypress', {{ key: 'Enter', code: 'Enter', keyCode: 13 }}  ) )
	"""

    driver.execute_script(js_command_page)

    html_source_code = driver.page_source

    with open(filename,'w') as outfile:
        
        outfile.write(html_source_code)   

