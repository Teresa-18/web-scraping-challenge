#!/usr/bin/env python
# coding: utf-8

# In[1]:

from bs4 import BeautifulSoup
from splinter import Browser
import requests
import pandas as pd

def scrape():


    # In[2]:
    executable_path = {'executable_path':'c:\\Users\\medinam\\Downloads\\chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    # In[3]:
    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[4]:
    results = soup.find_all('div', class_='list_text')[0]
    news_title = results.find('div', class_="content_title").text
    news_p = results.find('div', class_="article_teaser_body").text
    print(news_title)
    print(news_p)

    # In[5]:
    url = 'https://www.jpl.nasa.gov/images/'
    browser.visit(url)
    html = browser.html
    Soup = BeautifulSoup(html, "html.parser")


    # In[6]:
    image = Soup.find_all('img')[2]["src"]
    featured_image_url = image
    print(featured_image_url)


    # In[8]:
    mars_facts_url = "https://space-facts.com/mars/"
    browser.visit(mars_facts_url)
    tables = pd.read_html(mars_facts_url)
    mars_table = pd.DataFrame(tables[0])
    mars_facts = mars_table.to_html(header = True, index = False).replace ("<th>0</th>", "<th>Description</th>").replace ("<th>1</th>", "<th>Mars</th>")
    print(mars_facts)


    # # Mars Hemispheres

    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mars_hemisphere = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = products.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced","")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = downloads.find("a")["href"]
        mars_hemisphere.append({"title": title, "img_url": image_url})

    browser.quit()
# In[ ]:
    dictionary = {

        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": featured_image_url,
        "mars_facts": mars_facts,
        "mars_hemisphere": mars_hemisphere
    }

    return dictionary




