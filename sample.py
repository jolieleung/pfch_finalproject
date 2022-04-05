from selenium import webdriver
import glob

all_existing_html_files = list(glob.glob('html/*.html'))

driver = webdriver.Chrome(executable_path="./chromedriver")

driver.get('https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderProfileResults.aspx')


js_command = """
	document.getElementById('MainContentPlaceHolder_pagingUserControlTop_RecordsPerPage').value = 24;
	document.getElementById('MainContentPlaceHolder_pagingUserControlTop_RecordsPerPage').dispatchEvent( new Event('change') );
"""

driver.execute_script(js_command)

for page in range(355,357):


	filename = f'html/source_{page}.html'

	if filename in all_existing_html_files:
		print('Skipping page:',page)
		continue

	print('Doing page',page)

	js_command = f"""
		document.getElementById('MainContentPlaceHolder_pagingUserControlTop_pageTextBox').value = {page};
		document.getElementById('MainContentPlaceHolder_pagingUserControlTop_pageTextBox').dispatchEvent( new KeyboardEvent('keypress', {{ key: 'Enter', code: 'Enter', keyCode: 13 }}  ) )
	"""

	driver.execute_script(js_command)

	html_source_code = driver.page_source

	
	with open(filename,'w') as outfile:

		outfile.write(html_source_code)
