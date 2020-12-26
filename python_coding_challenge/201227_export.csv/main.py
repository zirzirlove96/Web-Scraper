import requests
from flask import Flask, render_template, request, send_file, redirect
import scrapper
"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""
app=Flask("JobScrapper")

@app.route("/")
def home():
  return render_template("home.html")

export_data=[]
@app.route("/search")
def search():
  global export_data
  parameter=request.args.get('term')
  if parameter:
    parameter=parameter.lower()
  dictionary1=scrapper.stackoverflow(parameter)
  dictionary2=scrapper.weworkremotely(parameter)
  dictionary3=scrapper.remoteok(parameter)
  #scrapper.save_to_file(scrapper.sum_dictionary(dictionary1,dictionary2,dictionary3))
  export_data = scrapper.sum_dictionary(dictionary1,dictionary2,dictionary3)
  size=len(dictionary1["data_set"])+len(dictionary2["data_set"])+len(dictionary3["data_set"])
  return render_template("search.html",parameter=parameter,
  size=size,dictionary1=dictionary1,dictionary2=dictionary2,dictionary3=dictionary3)

@app.route("/export")
def export():
  try:
    scrapper.save_to_file(export_data)
    return send_file("data.csv")
  except:
    return redirect("/")
  #return render_template("save.html")


app.run(host="0.0.0.0")