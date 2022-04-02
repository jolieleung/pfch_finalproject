import glob
from bs4 import BeautifulSoup
import json

all_files = glob.glob('html/*.html')

all_data = []

for file_name in all_files:
    #print(file_name)

    with open(file_name) as infile:

        html = infile.read()

        print(file_name)
        #print(html)

        soup = BeautifulSoup(html,'html.parser')

        for row in range(0,12):
            
            for left_or_right in ['Left', 'Right']:

                data={}
                
                use_id = f"MainContentPlaceHolder_SearchResultsList_SearchResultControl{left_or_right}_{row}_TaxonHTMLName_{row}"

                element = soup.find('a', {'id': use_id})

                #print(element.get_text().strip())

                data['plant_link'] = 'https://www.missouribotanicalgarden.org' + element['href']

                data['taxon_name']=element.get_text().strip()
            
                #print(data)
                all_data.append(data)

json.dump(all_data,open('all_data.json','w'), indent=2)