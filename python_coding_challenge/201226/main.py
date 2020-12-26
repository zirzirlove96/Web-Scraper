import requests
from flask import Flask, render_template, request
from scrapper import scrapper
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

@app.route("/search")
def search():
  parameter=request.args.get('term')
  if parameter:
    parameter=parameter.lower()
  dictionary=scrapper(parameter)
  size=len(dictionary["data_set"])
  return render_template("search.html",parameter=parameter,
  size=size,dictionary=dictionary)


app.run(host="0.0.0.0")