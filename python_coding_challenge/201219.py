import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")
url = "https://www.iban.com/currency-codes"
req = requests.get(url)
soup = BeautifulSoup(req.text,'html.parser')

tbody = soup.find('table')
tr = tbody.find_all('tr')
html_table={}
html_table["Country"]=[]
html_table["Code"]=[]

for index, value in enumerate(tr):
    if index>0:
        tds = value.find_all('td')
        if tds[2].text:
            html_table["Country"].append(tds[0].text.strip())
            html_table["Code"].append(tds[2].text.strip())
            

print("Welcome to CurrencyConvert PRO 2000")
print()
for i in range(len(html_table["Country"])):
    print("#",i,html_table["Country"][i])

print()
print("Where are you from? Choose a country by number.\n")

print("#: ",end=' ')
firstNumber = int(input())
print(html_table["Country"][firstNumber],'\n')

print("Now choose another country. \n")

print("#: ",end=' ')
secondNumber = int(input())
print(html_table["Country"][secondNumber],'\n')

while True:
  print("How many",html_table["Code"][firstNumber],"do you want to convert to",html_table["Code"][secondNumber])
  try:
    currency=int(input())#환전할 돈 입력
    url = "https://transferwise.com/gb/currency-converter"
    reqeusts = requests.get(f"{url}/{html_table['Code'][firstNumber]}-to-{html_table['Code'][secondNumber]}-rate?amount={currency}")
    #f{}를 사용하여 url에서 값을 넣어준다.
    soup = BeautifulSoup(reqeusts.text,"html.parser")
    div = soup.find("div",{"class":"col-lg-6 text-xs-center text-lg-left"})
    span = div.find("span",{"class":"text-success"})
    rate = currency*float(span.string)
    print(format_currency(currency,html_table["Code"][firstNumber],locale="ko_KR"),"is",format_currency(rate,html_table["Code"][secondNumber],locale="ko_KR"))
    break
  except ValueError:
    print("That wasn't a number.\n")
