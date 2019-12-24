import requests
import csv 

class Product : 
    def __init__(self):
        url="https://www.badmintonschlager.de/api/?route=export/feed&id=google_shopping&lang=de"
        resp= requests.get(url)
        with open("badminton.csv","wb") as f : 
            f.write(resp.content)
    def read_availability(self):
        with open("badminton.csv",'r') as f:
            csvfile =csv.reader(f,delimiter=",")
            for rows in csvfile :
                pass


products =Product();
products.read_availability();

