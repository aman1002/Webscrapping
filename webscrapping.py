
# coding: utf-8

# In[2]:

import requests
from bs4 import BeautifulSoup
import pandas


# In[3]:

base_url = "https://www.makaan.com/ghaziabad-property/raj-nagar-extension-flats-for-sale-51167"
l = []
for page in range(1,3):
    r = requests.get(base_url+"?page="+str(page))
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all = soup.find_all("div", {"class": "cardholder"})
    for item in all:
        d={}
        try:
            d["Seller"] = (item.find("span", {"class": "seller-name"}).text)
        except:
            d["Seller"] = None
        try:
            d["Bedroom"] = (item.find("strong", {"data-type": "listing-link"}).text)
        except:
            d["Bedroom"] = None
        try:
            d["Society"] = (item.find("span", {"itemprop": "alternateName"}).text)
        except:
            d["Society"] = None
        try:
            d["Locality"] = (item.find("span", {"itemprop": "addressLocality"}).text)
        except:
            d["Locality"] = None
        try:
            d["City"] = (item.find("span", {"itemprop": "addressRegion"}).text)
        except:
            d["City"] = None
        try:
            d["Price"] = (item.find("div", {"data-type": "price-link"}).text)
        except:
            d["Price"] = None
        try:
            d["Price per sq.ft"] = (item.find("div", {"class": "lbl rate"}).text)
        except:
            d["Price per sq.ft"] = None
        try:
            d["Size in Sq.Ft"] = (item.find("div", {"class": "size"}).text)
        except:
            d["Size in Sq.Ft"] = None
        try:
            d["Construction Status"] = (item.find("div", {"class": "val"}).text)
        except:
            d["Construction Status"] = None
        try:
            d["Bathrooms"] = (item.find("span", {"title": "Bathrooms"}).text)
        except:
            d["Bathrooms"] = None
        try:
            d["Floor"] = (item.find("span", {"title": "floor"}).text)
        except:
            d["Floor"] = None
        l.append(d)
print("Done")


# In[4]:

df = pandas.DataFrame(l)
df.to_excel("Output.xlsx")

