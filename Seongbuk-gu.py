##2016301016-김정재-
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import datetime
from selenium import webdriver
import time

def Store_analyze(result):
    URL = "http://market.koreacharts.com/store/11/11290/1129060000.html?&page="
    wd = webdriver.Chrome('D:/김정재/서경대학자료/서경대4학년/데이터크롤링/WebDriver/chromedriver.exe')


    for j in range(1, 133):
        wd.get(URL+str(j))
        time.sleep(0.5)
        
        if(j != 133):
            for i in range(0, 59, 6):
                try:
                    time.sleep(0.3)
                    html = wd.page_source
                    BS = BeautifulSoup(html, 'html.parser')
                    store_info = BS.select("div.box-body > table > tbody > tr > td.text-center")
            
                    store_info_list = list(store_info[0+i])##이름
                    store_name = store_info_list[1]
            
                    store_info_list = list(store_info[1+i])##업종분류
                    store_kinds = store_info_list[0]
            
                    store_info_list = list(store_info[2+i])##주소
                    store_address = store_info_list[0]

                    store_info_list = list(store_info[3+i])##전번
                    store_phone = store_info_list[0]

                    result.append([store_name]+[store_kinds]+[store_address]+[store_phone])
                except:
                    continue

        else:
            for i in range(0, 41, 6):
                try:
                    time.sleep(0.3)
                    html = wd.page_source
                    BS = BeautifulSoup(html, 'html.parser')
                    store_info = BS.select("div.box-body > table > tbody > tr > td.text-center")
            
                    store_info_list = list(store_info[0+i])
                    store_name = store_info_list[1]
            
                    store_info_list = list(store_info[1+i])
                    store_kinds = store_info_list[0]
            
                    store_info_list = list(store_info[2+i])
                    store_address = store_info_list[0]

                    store_info_list = list(store_info[3+i])
                    store_phone = store_info_list[0]

                    result.append([store_name]+[store_kinds]+[store_address]+[store_phone])
                except:
                    continue
                
    return
            

def main():
    result = []
    print('crawling >>>>>>>>>>>>>>>>>>>>>>>>')
    Store_analyze(result)

    SaTb = pd.DataFrame(result, columns = ('상호명', '업종분류', '주소', '전화번호'))
    SaTb.to_csv('./Seongbuk-gu.csv', encoding = 'cp949', mode = 'w', index = True)

if __name__ == '__main__':
    main()
