import requests
import os

def end():
    print("Do you wnat to start over? y/n",end=' ')
    answer=input()
    return answer

def start():

    print("Welcome to IsItDown.py!")
    print("Please write a URL or URLs you wnat to check. (suparated by comma)")
    research=input().replace(',',' ').split()#replace로 ,부분을 ' '로 바꿔준다.
    for urls in research:
        if '.com' not in urls.lower():#url값이 아닐 경우
            print(urls,"is not a valid url")
        else:
            if 'http://' not in urls.lower():
                url='http://'+urls.lower()
                r = requests.get(url)
                if r.status_code==200:
                    print(url,"is up!")
                elif r.status_code!=200:
                    print(url,"is down!")
            else:
                url=urls.lower()
                r=requests.get(url)
                if r.status_code==200:
                    print(url,"is up!")
                else:
                    print(url,"is down!")
            

start()
while True:

    result=end()
    if result=='y':
        os.system('clear')#console.log의 데이터를 지워준다.
        start()
    else:
        print("Bye!")
        break
