import requests
import csv 
import xml.etree.ElementTree as ET
import sys

skuList= []
class Product : 
    def __init__(self):
        pass
    def update_skuList(self):
        url="http://ec2-35-180-156-95.eu-west-3.compute.amazonaws.com/inventory/preorder/?fbclid=IwAR25jXqX0Peor-klBzHHMfW98SJFoYunnn4mk0hfQexfAKYnoV1DkqiFNk4"
        resp = requests.get(url)
        with open('skus.xml', 'wb') as f: 
            f.write(resp.content) 
    def update(self,url,i):
        resp= requests.get(url)
        with open("origFile"+str(i)+".csv","wb") as f : 
            f.write(resp.content)
    def check_availability(self,fileName,i):
        with open("origFile"+str(i)+".csv",'r',encoding='utf-8') as f:
            editFile= open(fileName,'w',newline="",encoding="utf-8") 
            editWriter=csv.writer(editFile)
            csvfile =csv.reader(f,delimiter="\t")
            for rows in csvfile :
                if (str(rows[0]).strip() in skuList) :
                    print(rows[0].strip(),end=" ")
                    rows[5]="preorder"
                editWriter.writerow(rows)
            editFile.close()
                    
    def read_xml(self):
        with open("skus.xml",encoding="utf-8") as f : 
            tree= ET.parse(f);
            root= tree.getroot();
            products=root.findall('./product')
            for i in products: 
                skuList.append(str(i.find('sku').text).strip())

url=[
"https://www.badmintonschlager.de/api/?route=export/feed&id=google_shopping&lang=de","https://www.onlinebadminton.co.uk/api/?route=export/feed&id=google_shopping",
"https://www.raquettedebadminton.fr/api/?route=export/feed&id=google_shopping",
"https://www.pestisport.hu/api/?route=export/feed&id=google_shopping&password=pestisport"]
names =[
"german_feed.csv","english_feed.csv","french_feed.csv",
"hungarian_feed.csv"]

products =Product();
products.update_skuList();
products.read_xml();
for i in range(len(url)):
    products.update(url[i],i)
    print(names[i])
    products.check_availability(names[i],i);

