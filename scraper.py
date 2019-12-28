import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
r= requests.get("https://seizoroi.com/eye/eyerackets.html?fbclid=IwAR1zJVTj36aRpvyokY-KvezoRNeak0kDt1M7IDmcAMzMgl_nubtvbt3-SjE")
soup = BeautifulSoup(r.content,'html.parser');
tables= soup.findAll('table')
data = ET.Element('products')
for table in tables: 
    rows= table.findAll('tr')
    for row in rows :
        columns=row.findAll('td')
        if(len(columns)==0):
            continue
        items = ET.SubElement(data, 'product')
        i=0
        sku=ET.SubElement(items,"sku")
        availability= ET.SubElement(items,"availability")
        for column in columns:
            if(i==4):
                sku.text=str(column.text).strip() 
                print(column.text)
            elif(i==6):
                availability.text=str(column.text).strip() 
            i+=1

mydata = ET.tostring(data)
myfile = open("scraped.xml", "wb")
myfile.write(mydata)
myfile.close()