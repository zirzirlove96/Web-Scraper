import csv

def save_to_file(jobs):
    file = open("jobs.csv",mode="w",encoding="utf-8")#파일을 열고, w는 쓰기, r 읽기
    writer = csv.writer(file)#파일 생성
    writer.writerow(["title", "company", "location", "link"])#행 생성
    for job in jobs:
        #print(list(job.values()))#dictionary에 있는 값만 가져와 준다
        writer.writerow(list(job.values()))#csv파일에 데이터 값들을 저장한다.
        #이는 list형식으로 저장해야 한다. 안 그러면 dict타입으로 저장됨
    #return 
