import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
from datetime import datetime
import random
from fake_useragent import UserAgent


ua = UserAgent()

headers = {
    'User-Agent': ua.random,
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}

session =  requests.Session()
session.headers.update(headers)

print("환경 설정이 완료되었습니다!")

url = "https://news.google.com/home?hl=ko&gl=KR&ceid=KR%3Ako"
reponse = session.get(url, headers= headers )
print(reponse.text)

def craw_nems_headline():
    base_url = "https://news.google.com/home?hl=ko&gl=KR&ceid=KR%3Ako"
    
    news_data = []
    
    
    
    
    try:
        reponse = session.get(base_url)
        reponse.raise_for_status()
        
        soup = BeautifulSoup(reponse.content, 'html.parser')
        
        headline = soup.find_all('h2', class_= 'headline' )
        
        
        for i ,headline in enumerate(headline, 1 ):
            news_item = {
                'title' : headline,
                'url' : f"hhttps://news.google.com/home?hl=ko&gl=KR&ceid=KR%3Ako,{i}",
                'crawl_tiem' : datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            news_data.append(news_item)
        print(f"✅ {len(news_data)}개의 뉴스 헤드라인 수집 완료!")
    except Exception as e:
         print(f"❌ 크롤링 중 오류 발생: {e}")
         
         
    return news_data

def save_newsdata(news_data):
    
    
    if news_data:
        df = pd.DataFrame(news_data)
        filename = f"news_headlines_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        df.to_csv(filename, index= False, encoding= 'utf-8-sig')
        print(f"✅ 데이터가 {filename}에 저장되었습니다.")
        return df
    else :
        print("❌ 저장할 데이터가 없습니다.")
        return None


news_data = craw_nems_headline()
df = save_newsdata(news_data)
if df is not None:
    print("\n📊 수집된 데이터 미리보기:")
    print(df.head())
        
