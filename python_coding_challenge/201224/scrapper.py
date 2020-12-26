import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def scrapper(data):
  url = f"https://www.reddit.com/r/{data}/top/?t=month"
  reqeusts=requests.get(url, headers=headers)
  soup = BeautifulSoup(reqeusts.text,"html.parser")
  div = soup.find("div",{"class":"rpBJOHq2PR60pnwJlUyP0"})
  subreddit_data={"data":[]}
  for setting in div:
    title = setting.find("h3",{"class":"_eYtD2XCVieq6emjKBH3m"})
    link = setting.find("a",{"class":"SQnoC3ObvgnGjWt90zD9Z _2INHSNB8V5eaWp4P0rY_mE"})
    upvotes = setting.find("div",{"class":"_1rZYMD_4xY3gRcSS3p8ODO"})
    if title and link and upvotes:
      subreddit_data["data"].append([title.string,
      link["href"],
      upvotes.string,
      data
      ])
     
  return subreddit_data
