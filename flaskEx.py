from flask import Flask,render_template,request,redirect,send_file
#request는 데이터를 웹사이트에 보내는 역할도 하게 된다.
from so import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")


#Fake DB는 라우트 외부에 있어야 한다.
db={}


@app.route("/")#/로 접속
def home():
    #return "Hello!!"#접속했을 경우 hello라는 문구가 뜨도록 서버를 연결해 준다.
    return render_template("index.html")#render_template을 사용하여 index.html을 사용하게 한다.

@app.route("/react")
def report():
    word = request.args.get('word')#index.html에서 입력폼에 입력한 값을 받아올 수 있는 함수.
    #return f"your are looking for a job in {word}"

    existingJobs = db.get(word)
    if existingJobs:#db에 이미 있으면
        jobs = existingJobs
    else:
        #db에 없으면 찾아서 db에 저장
        jobs = get_jobs(word)# so.py의 get_jobs 메서드를 사용
        db[word]=jobs
    if word=="":#입력 폼에 아무것도 입력하지 않았을 때 
        return redirect("/")
    return render_template(
        "report.html",
        number=len(jobs),
        searchingBy=word,
        jobs=jobs
    )#report.html에 값을 보내준다.


@app.route("/export")
def export():
    try:
        word = request.args.get("word")
        if not word:
            raise Exception()#word가 존재하지 않으면 except를 수행시킨다.
        jobs = db.get(word)
        if not jobs:
            raise Exception()#word가 있긴하나 db는 없다면
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")

"""
@app.route("/contact")
def contact():
    return "Contact!"#/contact 접속했을 경우
#@에 의해 바로 밑에 있는 함수만을 봐서 수행한다.
"""

"""
@app.route("/<username>")
def dynamic_urls(username):#dynamic urls를 사용하는 과정
    return f"{username}"
"""


app.run(host="0.0.0.0")#localhost:5000


