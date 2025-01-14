import requests
from bs4 import BeautifulSoup
import time

def get_html_text(link):
    req = requests.get(link)
    soup = BeautifulSoup(req.text, "html.parser")
    time.sleep(1)
    try:
        text = soup.text
    except:
        text = ''

    return text

if __name__=="__main__":
    link = 'https://stackabuse.com/guide-to-parsing-html-with-beautifulsoup-in-python/'
    print(get_html_text(link))