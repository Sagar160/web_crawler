import requests
from bs4 import BeautifulSoup
import re

def find_links_from_soup(soup, path):
    links = []
    for link in soup.findAll('a'):
        url=link.get('href')
        if url!='' and url!=None and (url[0]!='#') and url!="/":
            if 'https' not in url:
                url = path + url
            links.append(url)

    return links

def get_page_urls(link, keywords=[]):
    headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    req  = requests.get(link, headers=headers) 
    soup = BeautifulSoup(req.text, features="html.parser")
    urls = find_links_from_soup(soup, 'https://www.geminisolutions.com/')
    # print(urls)
    if keywords==[]:
        return urls
    else:
        valid_urls = []
        for url in urls:
            for key in keywords:            
                if key.lower() in url.lower():
                    valid_urls.append(url)

    return valid_urls

if __name__=="__main__":
    link = 'https://stackoverflow.com/questions/47928608/how-to-use-beautifulsoup-to-parse-google-search-results-in-python'
    print(get_page_urls(link, ['https:']))