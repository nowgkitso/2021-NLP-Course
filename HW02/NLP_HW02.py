import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
# 搜尋目前上映那些電影，擷取出其ID資訊
title_list = []
id_list = []
for i in range(10000):
    url = "https://movies.yahoo.com.tw/movieinfo_main/" + str(i)
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    #print(resp.text)
    soup = BeautifulSoup(resp.text, 'lxml')
    movie_html = soup.find("h1")
    print(i)
    if(movie_html != None):
        title_list.append(movie_html)
        id_list.append(i)
        print(movie_html)
df_movie_id = pd.DataFrame()
df_movie_id["電影"]=title_list
df_movie_id["ID"]=id_list
#存到檔案做備用
df_movie_id.to_csv("./movie.csv",encoding="utf-8-sig")