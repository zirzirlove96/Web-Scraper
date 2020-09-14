from indeed import extract_indeed_pages,extract_indeed_jobs
#indeed.py의 함수를 사용하기 위해

last_page = extract_indeed_pages()

print(extract_indeed_jobs(last_page))

