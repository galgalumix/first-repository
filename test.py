import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
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
