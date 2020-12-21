import os
import csv
import requests
from bs4 import BeautifulSoup

def save_to_file(a,alba):
  try:
    file=open(a+".csv",mode="w")
    writer = csv.writer(file)
    writer.writerow(["local","title","data","pay","regDate"])
    for value in alba:
      writer.writerow(list(value.values()))
  except FileNotFoundError:
    pass  


os.system("clear")
alba_url = "http://www.alba.co.kr/"
code_request = requests.get(alba_url)
codes_soup = BeautifulSoup(code_request.text, "html.parser")
alba_brands = codes_soup.find("div",{"id":"MainSuperBrand"})
super_brands = alba_brands.find("ul",{"class":"goodsBox"})
alba_sites=[]
for brands in super_brands.find_all("li",{"class":"impact"}):
    alba_sites.append([brands.find("a")["href"],
        brands.find("a").find("span",{"class":"company"}).get_text()])
   


for alba in alba_sites:
  url = requests.get(alba[0])
  soup = BeautifulSoup(url.text, "html.parser")
  table = soup.find("table")
  tbody = table.find("tbody")
  d=[]
#dictionary={}
  try:
    for tr in tbody.find_all("tr",{"class":""}):
      dictionary={}
      tds = list(tr.find_all("td"))
      dictionary["local"]=tds[0].text
      dictionary["title"]=tr.find("span",{"class":"company"}).text
      dictionary["data"]=tds[2].text
      dictionary["pay"]=tds[3].text
      dictionary["regDate"]=tds[4].text
      d.append(dictionary)
  except AttributeError:
    pass
  
  save_to_file(alba[1],d)#alba_sites에 저장한 place이름을 파일로 만들면서 dictionary에
  #저장한 알바에 대한 정보들을 csv파일에 저장해 준다.
     
