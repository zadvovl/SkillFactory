# This one needs to be iin a separate file because Jupyter
# doesn't allow multiprocessing on Windows and this is a way of
# bypassing this limitation

import pandas as pd
from bs4 import BeautifulSoup
import requests
import numpy as np
from datetime import datetime


def apply_to_dataframe(df):
    df_result = df.copy()
    df_result['all_review_dates'] = df_result['URL_TA'].apply(from_website)
    return df_result
	
	
def from_website(url):
    '''
    Gets additional data about the restaurant from tripadvisor 
    website if the proper url is provided.
    '''
    #print(f"https://www.tripadvisor.com{url}")
    u0 = f"https://www.tripadvisor.com{url}"
    r = requests.get(u0, timeout=600)
    soup = BeautifulSoup(r.content)
    a_lst = soup.find_all('a', {"class":"pageNum"})
    offs = []
    for a in a_lst:
        offs.append(a.attrs['data-offset'])
    
    rev_dates_lst = []

    for o in offs:    
        u = u0.replace('.html',f"-or{o}.html")
        r1 = requests.get(u, timeout=600)
        soup1 = BeautifulSoup(r1.content)

        tmp = soup1.find_all('span', {"class":"ratingDate"})
        rev_dates_lst = rev_dates_lst + [i['title'] for i in tmp]
    
    return rev_dates_lst
