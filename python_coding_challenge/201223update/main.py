import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"
new = f"{base_url}/search_by_date?tags=story"
popular = f"{base_url}/search?tags=story"


def make_detail_url(id):
    return f"{base_url}/items/{id}"


db = {}
app = Flask("DayNine")


@app.route("/")
def home():
  parameter = request.args.get('order_by','popular')
  #db에 parameter가 잇는지 확인해야함
  if parameter not in db:
    if parameter == 'popular':
      page = requests.get(popular)
    elif parameter == 'new':
      page = requests.get(new)
    db[parameter]=page.json()['hits']#가짜 DB에 json타입으로 넣어주고
   
    #print(db[parameter])
  db_contents = db[parameter]
  return render_template("index.html",order_by=parameter,result=db_contents)


@app.route("/<id>")
def detail(id):
  detail_request = requests.get(make_detail_url(id))
  result = detail_request.json()
  return render_template("detail.html",result=result)


app.run(host="0.0.0.0")
