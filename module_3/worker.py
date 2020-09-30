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
    r = requests.get(f"https://www.tripadvisor.com{url}", timeout=20)
    soup = BeautifulSoup(r.content)
    
    tmp = soup.find_all('span', {"class":"ratingDate"})
    rev_dates_lst = [i['title'] for i in tmp]
    
    return rev_dates_lst	