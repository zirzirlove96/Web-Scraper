from flask import Flask,render_template,request,redirect
#request는 데이터를 웹사이트에 보내는 역할도 하게 된다.
from so import get_jobs


app = Flask("SuperScrapper")

@app.route("/")#/로 접속
def home():
    #return "Hello!!"#접속했을 경우 hello라는 문구가 뜨도록 서버를 연결해 준다.
    return render_template("index.html")#render_template을 사용하여 index.html을 사용하게 한다.

@app.route("/react")
def report():
    word = request.args.get('word')#index.html에서 입력폼에 입력한 값을 받아올 수 있는 함수.
    #return f"your are looking for a job in {word}"
    jobs = get_jobs(word)
    """ so.py의 get_jobs 메서드를 사용 """
    print(jobs)
    if word=="":#입력 폼에 아무것도 입력하지 않았을 때 
        return redirect("/")
    return render_template("report.html",searchingBy=word)#report.html에 값을 보내준다.

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

