import requests #url를 요청할 수 있다.
#request를 먼저 설치해 준다.
from bs4 import BeautifulSoup

indeed_requests = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
#html 정보를 모두 가져온다.

indeed_soup = BeautifulSoup(indeed_requests.text, "html.parser")
#indeed_requests.text의 정보에서 html에 들어간 코드만 추출

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all('a')

pages=[]
for link in links[:-1] :
  pages.append(int(link.string))
  
max_page = pages[-1]
#마지막 next를 빼기 위해
#페이지 수를 출력하는 과정
