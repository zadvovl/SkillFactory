import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
from itertools import product
import json

def crawl_auto_parallel(out_list, brands, year_from=1980, year_to=2021, fr=0, to=10000000, radius=200):
    """
    This function crawls auto.ru. Idea for this function was 
    taken from https://github.com/DarkLabel1/YouTube/blob/master/Auto_ru.py
    
    After that it was slightly modified to fit the requirements of kaggle competition
    
    Arguments:
        brands - a list of brands to process
        year_from and year_to - range of car production years
        fr and to - used for testing (you can slice year_brand list to make the output longer or shorter
        if you need to test something)
        radius - radius from Moscow
    """
    print('I am here')
    
    # all the years to consider
    year_range = list(np.arange(year_from, year_to))
    
    # pairs of year and brand to iterate over them
    year_brand = list(product(year_range, list(df_brands['Brands'])))
    year_brand    
    
    # these 2 won't change
    URL = 'https://auto.ru/-/ajax/desktop/listing/' #URL for the post request

    # header for the post request
    HEADERS = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Content-Length': '137',
        'content-type': 'application/json',
        'Cookie': 'autoru_gdpr=1; _csrf_token=1c0ed592ec162073ac34d79ce511f0e50d195f763abd8c24; autoru_sid=a%3Ag5e3b198b299o5jhpv6nlk0ro4daqbpf.fa3630dbc880ea80147c661111fb3270%7C1580931467355.604800.8HnYnADZ6dSuzP1gctE0Fw.cd59AHgDSjoJxSYHCHfDUoj-f2orbR5pKj6U0ddu1G4; autoruuid=g5e3b198b299o5jhpv6nlk0ro4daqbpf.fa3630dbc880ea80147c661111fb3270; suid=48a075680eac323f3f9ad5304157467a.bc50c5bde34519f174ccdba0bd791787; from_lifetime=1580933172327; from=yandex; X-Vertis-DC=myt; crookie=bp+bI7U7P7sm6q0mpUwAgWZrbzx3jePMKp8OPHqMwu9FdPseXCTs3bUqyAjp1fRRTDJ9Z5RZEdQLKToDLIpc7dWxb90=; cmtchd=MTU4MDkzMTQ3MjU0NQ==; yandexuid=1758388111580931457; bltsr=1; navigation_promo_seen-recalls=true',
        'Host': 'auto.ru',
        'origin': 'https://auto.ru',
        'Referer': 'https://auto.ru/ryazan/cars/mercedes/all/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'x-client-app-version': '202002.03.092255',
        'x-client-date': '1580933207763',
        'x-csrf-token': '1c0ed592ec162073ac34d79ce511f0e50d195f763abd8c24',
        'x-page-request-id': '60142cd4f0c0edf51f96fd0134c6f02a',
        'x-requested-with': 'fetch'
    }    
    
    for yb in year_brand[fr:to]:  
        i = 1 # initializing i for pagination 
        l = 1 # initializing l that will be replaced by len(data) below
        while l > 0:
            # Post request parameters are changed within the loop
            PARAMS = {
                 'catalog_filter' : [{"mark": yb[1]}],
                 'section': "all",
                 'category': "cars",
                 'sort': "fresh_relevance_1-desc",
                 'page': i,
                 'geo_radius' : str(radius),
                 'year_from' : str(yb[0]),
                 'year_to' : str(yb[0]),
                 'geo_id' : [213]
                }

            i+=1

            response = requests.post(URL, json=PARAMS, headers=HEADERS) 
            data = response.json()['offers']
            l = len(data)
            if l > 0:
                print(f'{yb[1]}, year {yb[0]} : {i} entries')
                for o in data:
                    out_list.append(o)
    
    print('Crawling done!!!')  