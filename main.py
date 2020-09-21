from indeed import get_jobs as get_indeed_jobs
#indeed.py의 함수를 사용하기 위해
from so import get_jobs as get_so_jobs
from save import save_to_file #csv로 변환해주는 save.py

indeed_jobs = get_indeed_jobs()#indeed 웹
so_jobs = get_so_jobs()#stackoverflow 웹


#jobs = indeed_jobs+so_jobs
jobs = so_jobs #stackoverflow페이지만
jobs = indeed_jobs+so_jobs


save_to_file(jobs)


