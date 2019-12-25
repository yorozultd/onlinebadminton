import requests
import csv 
import xml.etree.ElementTree as ET
skuList= []
class Product : 
    def __init__(self):
        pass
    def update(self):
        url="https://www.badmintonschlager.de/api/?route=export/feed&id=google_shopping&lang=de"
        resp= requests.get(url)
        with open("badminton.csv","wb") as f : 
            f.write(resp.content)
        url="http://ec2-35-180-156-95.eu-west-3.compute.amazonaws.com/inventory/preorder/?fbclid=IwAR25jXqX0Peor-klBzHHMfW98SJFoYunnn4mk0hfQexfAKYnoV1DkqiFNk4"
        resp = requests.get(url)
        with open('skus.xml', 'wb') as f: 
            f.write(resp.content) 
    def check_availability(self):
        with open("badminton.csv",'r') as f:
            editFile= open("output.csv",'w',newline="") 
            editWriter=csv.writer(editFile)
            csvfile =csv.reader(f,delimiter="\t")
            for rows in csvfile :
                if (str(rows[0]).strip() in skuList) :
                    print(rows[0].strip())
                    rows[5]="preorder"
                editWriter.writerow(rows)
            editFile.close()
                    
    def read_xml(self):
        with open("skus.xml",encoding="utf8") as f : 
            tree= ET.parse(f);
            root= tree.getroot();
            products=root.findall('./product')
            for i in products: 
                skuList.append(str(i.find('sku').text).strip())

products =Product();
#products.update()
products.read_xml();
#print(skuList)
products.check_availability();

