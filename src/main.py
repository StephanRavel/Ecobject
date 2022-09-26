


    
# récupérer le HTML en brut 
URL = "https://www.co2everything.com/a-z"
res = requests.get(URL)
#print(r.content)

# parser le code HTML 
soup = BeautifulSoup(res.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
#print(soup.prettify())

products=[]  # a liste des produits ou objets 

# chercher toutes les balises de type 'a' avec l'attribut spécifié    
table = soup.findAll('a', attrs = {'class':'graphdiv w-inline-block'}) 
print(len(table))

# pour chaque ligne de table, on stocke les informations qui nous intéressent 
for row in table:
    object = {}
    object ['product_name'] = row.find('div', attrs = {'class':'graphitemname'}).text
    object ['co2_footprint'] = row.find('div', attrs = {'class':'kmtext'}).text
    object ['units'] = row.find('div', attrs = {'class':'kmtextfigure'}).text
    products.append(object)
