import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
URL = "https://www.iban.com/currency-codes"
html_table={}

def solution():
  url = requests.get(URL)
  global html_table

  soup = BeautifulSoup(url.text, "html.parser")

  table = soup.find('table',{'class':'table table-bordered downloads tablesorter'})
  #바로 table을 찾아준다.
  #table->tr->td

  trs = table.find_all('tr')

  #Country, Code만 필요로 하다.
  html_table["Country"]=[]
  html_table["Code"]=[]


  for idx,tr in enumerate(trs):#index값과 tr안에 있는 값을 가져온다.
      if idx>0:
          tds = tr.find_all('td')
          if tds[2].text:#Code에 비어있지 않으면
            html_table["Country"].append(tds[0].text.strip())
            html_table["Code"].append(tds[2].text.strip())
  return html_table




print("Hello! Please choose select a country by number : ")
currency_of_list=solution()
for i in range(len(currency_of_list["Country"])):
  print("#",i,currency_of_list["Country"][i])

while True:
  print("#:",end='')
  s = input()
  try:
    num = int(s)
    if num>len(currency_of_list["Country"]) or num<0:
      print("Choose a number from the list.")
    else:
      print("You chose",currency_of_list["Country"][num])
      print("The currency code is",currency_of_list["Code"][num])
      break
  except:
      print("That wasn't a number.")

    
