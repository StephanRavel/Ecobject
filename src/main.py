# from itertools import product
from math import prod
from funcs import *

def main():
    URL = 'https://www.co2everything.com/a-z'
    soup = get_soup(URL)
    products = get_all_products (soup)
    write_products_csv(products)

if __name__=="__main__":
    main()
