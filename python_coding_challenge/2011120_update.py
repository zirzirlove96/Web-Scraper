import os
import requests
from bs4 import BeautifulSoup

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
            

print("Hello Please choose select a country by number: ")
for i in range(len(html_table["Country"])):
    print("#",i,html_table["Country"][i])

while True:
    print("#:",end=' ')
    try:
        answer=input()
        if type(int(answer)) is int:
            if int(answer)>len(html_table["Country"]):
                print("Choose a number from the list.")
            else:
                result1=html_table["Country"][int(answer)]
                result2=html_table["Code"][int(answer)]
                print("You chose",result1)
                print("The currency code is",result2)
                break
    except ValueError:
        print("That wasn't a number.")
