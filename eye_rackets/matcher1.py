import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import numpy

r= requests.get("https://seizoroi.com/eye/eyerackets.html?fbclid=IwAR1zJVTj36aRpvyokY-KvezoRNeak0kDt1M7IDmcAMzMgl_nubtvbt3-SjE")
soup = BeautifulSoup(r.content,'html.parser');
tables= soup.findAll('table')
gtin_website= []
for table in tables: 
    rows= table.findAll('tr')
    for row in rows :
        columns=row.findAll('td')
        if(len(columns)==0):
            continue
        i=0
        for column in columns:
            if(i==4):
                gtin_website.append(str(column.text).strip())

to_be_disabled=[]
preorder_url ="http://ec2-35-180-156-95.eu-west-3.compute.amazonaws.com/inventory/preorder/?fbclid=IwAR1WuNCGZtLD4h4tdFcmtlD2oGDBWcO-nWKA8vH4_bW42xXfcTNlG4L5USY"
pr=requests.get(preorder_url)
with open("preorder.xml") as f1:
    f1.write(pr.content)
preorderxml = open("preorder.xml")
tree= ET.parse(preorderxml)
root = tree.getroot();
products = root.findall("./product")
for product in products : 
    filegtin=str(product.find('gtin').text).strip() 
    hashvalue=str(product.find('hash').text).strip() 
    if(filegtin in gtin_website) :
        pass
    else:
        to_be_disabled.append(hashvalue)

