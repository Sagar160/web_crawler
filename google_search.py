from googlesearch import search
import requests
from bs4 import BeautifulSoup
import urllib


# def get_search(query, res_num=10):
#     urls = [url for url in search(query, stop=res_num, pause=5)]
#     return urls

def get_search(query):
    # text = query.replace(" ", "+")
    text = urllib.parse.quote_plus(query)
    link = 'https://google.com/search?q=' + text
    print(f'google search url: {link}')
    
    headers = {
    'User-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }
    req  = requests.get(link, headers=headers)
    soup = BeautifulSoup(req.text, features="html.parser")
    search_tags = soup.findAll('a')
    urls = []
    headings = []
    print(soup)
    for tag in search_tags:
        heading = tag.find( 'h3' )
        if heading!=None:
            urls.append(tag.get('href'))
            headings.append(heading.getText())
    return urls, heading

if __name__=="__main__":
    print(get_search('gemini soplutions'))