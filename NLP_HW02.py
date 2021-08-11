import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
# 搜尋目前上映那些電影，擷取出其ID資訊
for i in range(100):
    url = "https://movies.yahoo.com.tw/movieinfo_main/" + str(i)
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    #print(resp.text)
    soup = BeautifulSoup(resp.text, 'lxml')
    movie_html = soup.find("h1")
    print(movie_html)