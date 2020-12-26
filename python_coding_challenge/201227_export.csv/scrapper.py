import requests
from bs4 import BeautifulSoup
import csv


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def sum_dictionary(data_set1,data_set2,data_set3):
  data_set= {**data_set1, **data_set2, **data_set3}
  return data_set

def save_to_file(data):
  try:
    file=open("data.csv",mode="w",encoding="utf-8")
    writer = csv.writer(file)
    writer.writerow(["title","company","url"])
    for value in data.values():
      for data in value:
        writer.writerow([data[0],data[1],data[2]])
  except FileNotFoundError:
    pass

def stackoverflow(data):
  url=f"https://stackoverflow.com/jobs?q={data}&r=true"
  html=requests.get(url,headers=headers)
  soup = BeautifulSoup(html.text, "html.parser")
  listResult = soup.find("div",{"class":"listResults"})  
  dictionary = {
    "data_set":[]
    }
  listResult = soup.find("div",{"class":"listResults"})
  title = listResult.find_all("a", {"class":"s-link stretched-link"}) 
  company = listResult.find_all("span",{"class":None})
  list1,list2,list3=[],[],[]
  for t in title:
    if t:
      list1.append(t.string)
  for c in company:
    if c:
      list2.append(c.string)
  for link in title:
    if link:
      list3.append(link["href"])
  for i in range(len(list1)):
    dictionary["data_set"].append([list1[i],list2[i],list3[i]])
  return dictionary


def weworkremotely(data):
  url = f"https://weworkremotely.com/remote-jobs/search?term={data}"
  html = requests.get(url,headers=headers)
  soup=BeautifulSoup(html.text,"html.parser")
  data_set={
    "data_set":[]
    }

  li=soup.find_all("li",{"class":"feature"})
 
  for span in li:  
    data_set["data_set"].append([span.find("span",{"class":"title"}),span.find("span",{"class":"company"}).string.string,span.select_one("li>a")["href"]])

  return data_set


def remoteok(data):
  url = f"https://remoteok.io/remote-dev+{data}-jobs"
  html = requests.get(url,headers=headers)
  soup=BeautifulSoup(html.text,"html.parser")
  td = soup.find_all("td",{"class":"company position company_and_position"})
  remoteok_data = {
    "data_set":[]
    }
  for data in td:
    title = data.find("h2",{"itemprop":"title"})
    company = data.find("h3",{"itemprop":"name"})
    if title and company:
      remoteok_data["data_set"].append([title.string,company.string,
                                        data.find("a",{"class":"preventLink"})["href"]])

  return remoteok_data

#save_to_file(sum_dictionary(stackoverflow("python"),weworkremotely#("python"),remoteok("python")))
