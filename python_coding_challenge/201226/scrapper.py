import requests
from bs4 import BeautifulSoup


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def scrapper(data):
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
