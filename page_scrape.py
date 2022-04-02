from cgitb import html
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.missouribotanicalgarden.org/PlantFinder/PlantFinderProfileResults.aspx?cv=5&chr=32')

# with open(r'Final_Project\abutilon.html',encoding="utf-8") as html_file:
#     abutilon = html_file.read()
    #print(abutilon) - test

    soup = BeautifulSoup(abutilon, 'lxml')
    # #print(soup.prettify()) - test


    # characteristics_html_tags = soup.find_all('div')
    # #print(tags)

    # for characteristics in characteristics_html_tags:
    #     print(characteristics.text)

    # type_text = soup.find_all('div', class_='row', id="MainContentPlaceHolder_TypeRow")
    # for type in type_text:
    #      print(type.text)

    # zone_text = soup.find_all('div', class_='row', id="MainContentPlaceHolder_ZoneRow")
    # for zone in zone_text:
    #      print(zone.text)

    # height_text = soup.find_all('div', class_='row', id="MainContentPlaceHolder_HeightRow")
    # for height in height_text:
    #      print(height.text)


    plants = soup.find_all('a', id = "MainContentPlaceHolder_SearchResultsList_SearchResultControlLeft_0_TaxonHTMLName_0")

    scientific_name = soup.find('title').text.replace('  ','')
    common_name = soup.find('div', class_='row', id="MainContentPlaceHolder_CommonNameRow").text.replace('  ','')
    type = soup.find('div', class_='row', id="MainContentPlaceHolder_TypeRow").text.replace('  ','')
    zone = soup.find('div', class_='row', id="MainContentPlaceHolder_ZoneRow").text.replace('  ','')
    height = soup.find('div', class_='row', id="MainContentPlaceHolder_HeightRow").text.replace('  ','')
    spread = soup.find('div', class_='row', id="MainContentPlaceHolder_SpreadRow").text.replace('  ','')
    bloom_time = soup.find('div', class_='row', id="MainContentPlaceHolder_BloomTimeRow").text.replace('  ','')
    bloom_desc = soup.find('div', class_='row', id="MainContentPlaceHolder_ColorTextRow").text.replace('  ','')
    sun = soup.find('div', class_='row', id="MainContentPlaceHolder_SunRow").text.replace('  ','')
    water = soup.find('div', class_='row', id="MainContentPlaceHolder_WaterRow").text.replace('  ','')
    maintenance = soup.find('div', class_='row', id="MainContentPlaceHolder_MaintenanceRow").text.replace('  ','')

    print(scientific_name)
    print(common_name)
    print(type)
    print(zone)
    print(height)
    print(spread)
    print(bloom_time)
    print(bloom_desc)
    print(sun)
    print(water)
    print(maintenance)