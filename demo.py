import requests
import csv
import uuid
from requests_html import HTMLSession
from datetime import date
s = HTMLSession()


# ----------------------------------- Functions -------------------------------------------


# def get_products_links(page):
#     url = f'https://plugintheme.net/product-category/wordpress-themes/page/{page}/'
#     links = []
#     r = s.get(url)
#     products = r.html.find('.product-title')
#     for item in products:
#         links.append(item.find('a', first=True).attrs['href'])
#     return links

url = 'https://plugintheme.net/shop/betheme-responsive-multi-purpose-wordpress-theme/'

def parse_products(url):

    r = s.get(url)

    product_details = {
        'f_des': r,
    }
    return product_details

print(parse_products(url))


