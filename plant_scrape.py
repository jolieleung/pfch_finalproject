import glob
from bs4 import BeautifulSoup
import json
import requests

with open(r'C:\Users\leung\OneDrive\Desktop\pfch_finalproject\all_search_data.json','r') as all_search_data:

    all_search = json.load(all_search_data)

    all_plant_data = []

    #print(plant['plant_link'])


    
    for plant in all_search:
            
        url = plant['plant_link']
        #print(html_text)

        r = requests.get(url)
        #print(html_text.text)

        if r.status_code == 200:
            print('This works: ', url)

            # scientific_name = None
            # common_name = None
            # type = None
            # family = None
            # native_range = None
            # zone = None
            # height = None
            # spread = None
            # bloom_time = None
            # bloom_desc = None
            # sun = None
            # water = None
            # maintenance = None
        
        else: 
            print('No page found')

        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup.prettify())

        plant_data = soup.find_all('div')
        #print(plant_data)

        plant_data_entries={}
        
        scientific_name = soup.find('span', id = "dnn_srTitle_lblTitle").text
        #print('Scientific Name: ' + scientific_name)
        
        plant_data_entries['ScientificName'] = scientific_name.strip()

        
        for field in ['CommonNameRow', 'TypeRow', 'FamilyRow','NativeRangeRow','ZoneRow', 'HeightRow', 'SpreadRow', 'BloomTimeRow','ColorTextRow','SunRow','WaterRow','MaintenanceRow']:
            
            use_id = f"MainContentPlaceHolder_{field}"

            element = soup.find('div', {'id': use_id})
            #print(element)

            if element != None:

                plant_data_entries[field] = element.get_text().strip()
                #print(element.get_text().strip())
                #all_plant_data.append(data)
            
            # else:
            #     print(f"{row_type} not found")
        
        plant_data_entries['URL'] = url

        print(plant_data_entries)
        
        
        all_plant_data.append(plant_data_entries) 

                
json.dump(all_plant_data,open('all_plant_data.json','w'), indent=2)

