import requests
from bs4 import BeautifulSoup

#LIMIT=50 stackoverflow페이지는 limit을 사용하지 않는다.
URL=f"https://stackoverflow.com/jobs?q=python&pg=2"

#페이지를 추출하기
def get_jobs() :
    last_page = get_last_page()
    
