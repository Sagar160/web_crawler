import os
import time
import pandas as pd
from google_search import get_search
from url_search import get_page_urls
from parse_html import get_html_text

def web_crawler(url_keywords, output_dir, links):
    # if link!=None:
    #     return get_html_text(link)

    # default value is top 10 urls
    # google_search_urls = get_search(query)
    # print('google search complete')

    # search urls for each pages
    all_urls = links
    for url in links:
        all_urls = all_urls + get_page_urls(url, url_keywords)
        time.sleep(1)
    print('find all urls at depth 1')

    # parse links
    unique_urls = list(set(all_urls))
    print(unique_urls)

    df_res = pd.DataFrame()
    df_res['link']    = unique_urls
    df_res['content'] = df_res['link'].apply(lambda x: get_html_text(x))
    print('text extraction complete')

    timestr  = time.strftime("%Y%m%d-%H%M%S")
    filename = f"result_{timestr}.csv"
    df_res.to_csv(os.path.join(output_dir, filename))
    print('output file saved')

if __name__=="__main__":
    query        = "Gemini Solutions"
    links        = ['https://www.geminisolutions.com/',
                    'https://in.linkedin.com/company/gemini-solutions-india',
                    'https://www.glassdoor.co.in/Overview/Working-at-Gemini-Solutions-EI_IE1333027.11,27.htm',
                    'https://www.ambitionbox.com/overview/gemini-solutions-overview',
                    ]
    url_keywords = ['https:', 'gemini']
    output_dir   = r'C:\Users\sagar.panwar\Documents\projects\web_crawler\data'
    web_crawler(url_keywords, output_dir, links)