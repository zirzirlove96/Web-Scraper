from flask import Flask,render_template


app = Flask("SuperScrapper")

@app.route("/")#/로 접속
def home():
    #return "Hello!!"#접속했을 경우 hello라는 문구가 뜨도록 서버를 연결해 준다.
    return render_template("index.html")#render_template을 사용하여 index.html을 사용하게 한다.

@app.route("/contact")
def contact():
    return "Contact!"#/contact 접속했을 경우
#@에 의해 바로 밑에 있는 함수만을 봐서 수행한다.

"""
@app.route("/<username>")
def dynamic_urls(username):#dynamic urls를 사용하는 과정
    return f"{username}"
"""


app.run(host="0.0.0.0")#localhost:5000


