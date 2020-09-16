import requests
from bs4 import BeautifulSoup

#LIMIT=50 stackoverflow페이지는 limit을 사용하지 않는다.
URL=f"https://stackoverflow.com/jobs?q=python&sort=i"

#마지막 페이지를 반환하는 함수 
def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div",{"class":"s-pagination"}).find_all("a")
    #div요소의 class이름이 s-pagination인 곳에서 모든 a태그를 가져온다.
    last_page = pages[-2].get_text(strip=True)#Next표시를 없애고 마지막 페이지까지만 가져오기 위해
    #string대신 get_text()를 사용하여 숫자만 가져오고 빈 여백을 없애기 위해 strip=True를 해준다.
    return int(last_page)


#직무 반환
def extract_job(html):
    title = html.find("div", {"class":"fl1"}).find("h2").find("a")["title"]#직무 이름
    #회사명과 위치 
    company,location = html.find("div",{"class":"fl1"}).find("h3").find_all("span",recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip("-")
    #print(company, location)
    job_id = html["data-jobid"]#지원서 링크 
    
    return {"title":title,
            "company":company,
            "location":location,
            "link": f"https://stackoverflow.com/jobs/{job_id}"}
    

#페이지에 대한 직업들 추출하는 함수(-job은 extract_job의 함수에서 반환하는 데이터가 있는 곳이다. )
def extract_jobs(last_page):
    jobs=[]
    for page in range(last_page):
        print(f"StackOverflow Web Scraping {page}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text,"html.parser")
        results = soup.find_all("div",{"class":"-job"})
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs
    


#페이지를 추출하기
def get_jobs() :
    last_page = get_last_page()
    jobs = extract_jobs(20)
    return jobs
    
