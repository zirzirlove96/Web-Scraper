from flask import Flask,render_template,request
#request는 데이터를 웹사이트에 보내는 역할도 하게 된다.


app = Flask("SuperScrapper")

@app.route("/")#/로 접속
def home():
    #return "Hello!!"#접속했을 경우 hello라는 문구가 뜨도록 서버를 연결해 준다.
    return render_template("index.html")#render_template을 사용하여 index.html을 사용하게 한다.

@app.route("/react")
def react():
    word = request.args.get("word")#index.html에서 입력폼에 입력한 값을 받아올 수 있는 함수.
    #return f"your are looking for a job in {word}"
    return render_template("react.html",searchingBy=word)#react.html에 단어를 보내준다.

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


