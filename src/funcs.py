import requests
import requests
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
    products={}  # a liste des produits ou objets 
    # chercher toutes les balises de type 'a' avec l'attribut spécifié    
    table = soup.findAll('a', attrs = {'class':'graphdiv w-inline-block'}) 
    nb_objects = len(table)
    # pour chaque ligne de table, on stocke les informations qui nous intéressent 
    for (row,i) in (table, range(1, nb_objects + 1)):
        object = {}
        object ['id'] = i
        object ['product_name'] = row.find('div', attrs = {'class':'graphitemname'}).text
        object ['co2_footprint'] = row.find('div', attrs = {'class':'kmtext'}).text
        object ['units'] = row.find('div', attrs = {'class':'kmtextfigure'}).text
        products.update(object)
    return products

 





    

