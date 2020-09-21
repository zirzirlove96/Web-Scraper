import csv

def save_to_file(jobs):
    file = open("export.csv",mode="w",encoding="utf-8")
    writer = csv.writer(file)#파일 생성
    writer.writerow(["title", "company", "location", "link"])#행 생성
    for job in jobs:
        writer.writerow(list(job.values()))#csv파일에 데이터 값들을 저장한다.
