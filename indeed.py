import requests
from bs4 import BeautifulSoup
#url를 요청할 수 있다.
#request를 먼저 설치해 준다.

LIMIT = 50 #start번호
INDEED_URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"

def extract_indeed_pages():
    result = requests.get(INDEED_URL)
    #html 정보를 모두 가져온다.
    soup = BeautifulSoup(result.text, "html.parser")
    ##indeed_requests.text의 정보에서 html에 들어간 코드만 추출

    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all('a')

    pages=[]
    for link in links[:-1] :
      pages.append(int(link.string))
  
    max_page = pages[-1]#마지막 next를 빼기 위해
#페이지 수를 출력하는 과정
    return max_page

def extract_job(html):
    #div태스의 title요소를 찾아 글의 제목 추출
    title = html.find("a")["title"]
    #회사명 추출 
    company = html.find("span",{"class":"company"})
    company_anchor=company.find("a")
    if company_anchor is not None:
        company=str(company_anchor.string)
    else:
        company=str(company.string)
    company = company.strip()
    location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]
    job_id=html["data-jk"]
    return {"title":title,
            "company" : company,
            "location" : location,
            "link" : f"https://www.indeed.com/viewjob?jk={job_id}"}
    


def extract_indeed_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Web Scraping {page}")
        #print(f"&start={page*LIMIT}")#페이지의 수를 구할 수 있는 함수
        result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class" : "jobsearch-SerpJobCard"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs
