import requests
from bs4 import BeautifulSoup

#LIMIT=50 stackoverflow페이지는 limit을 사용하지 않는다.
URL=f"https://stackoverflow.com/jobs?q=python&pg=2"

#마지막 페이지를 반환하는 함수 
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
    #div요소의 class이름이 s-pagination인 곳에서 a태그를 가지고 있는 모두를 가져온다.
    last_page = pages[-2].get_text(strip=True)#Next표시를 없애고 마지막 페이지까지만 가져오기 위해
    #string대신 get_text()를 사용하여 숫자만 가져오고 빈 여백을 없애기 위해 strip=True를 해준다.
    return last_page
    


#페이지를 추출하기
def get_jobs() :
    last_page = get_last_page()
    print(last_page)
    return []
    
