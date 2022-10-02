import requests
import requests
import json 
import csv
from bs4 import BeautifulSoup

def get_soup(URL):
    # récupérer le HTML en brut 
    # URL = "https://www.co2everything.com/a-z"
    res = requests.get(URL)
    # parser le code HTML 
    soup = BeautifulSoup(res.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
    #print(soup.prettify())
    return soup 

def get_all_products(soup):
    products=[]  # a liste des produits ou objets 
    # chercher toutes les balises de type 'a' avec l'attribut spécifié    
    table = soup.findAll('a', attrs = {'class':'graphdiv w-inline-block'}) 
    # nb_objects = len(table)
    i=0
    # pour chaque ligne de table, on stocke les informations qui nous intéressent 
    for row in table:
        object = {}
        i+=1
        object['id'] = i
        object ['product_name'] = row.find('div', attrs = {'class':'graphitemname'}).text
        object ['co2_footprint'] = row.find('div', attrs = {'class':'kmtext'}).text
        object ['units'] = row.find('div', attrs = {'class':'kmtextfigure'}).text
        # products['id'] = i
        products.append(object)
    return products

def write_products_json(products):
    with open('./data/products.json', 'w', encoding='utf-8') as f:
        json.dump(products, f, ensure_ascii=False, indent=4)

def write_products_csv(products):
    # get all headers
    prod_keys = products[0].keys()
    headers=[]
    for header in prod_keys:
        headers.append(header)

    # create products csv files 
    with open('./data/products.csv', 'w',newline='', encoding='UTF8') as f:
        writer = csv.writer(f)

        #write headers: 
        writer.writerow(headers)

        #write data
        for prod_line in products:
            row=[]
            for prod in prod_line.values():
                row.append(prod)
            writer.writerow(row)


 





    

