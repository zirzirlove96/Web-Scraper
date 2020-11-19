import requests
import os


def end():

    print("Do you want to start over? y/n")
    answer=input()
    return answer

def start():
    
    while True:
        print("Welcome to IsItDown.py!\nPlease write a URL or URLs you wnat to check. (separated bt comma)")
        urls = input().replace(' ','').split(',')
        for url in urls:
            if '.com' not in url.lower():
                print(url,"is not a valid url")
            else:
                url = "http://"+url.lower()
                r = requests.get(url)
                if r.status_code==200 and 'http://' in url:
                    print(url,'is up!')
                elif r.status_code==200 and 'http://' not in url:
                    print('http://',url,'is up!')
                elif r.status_code!=200 and 'http://' not in url:
                    print('http://',url,'is down!')
                elif r.status_code!=200 and 'http://' in url:
                    print(url,'is down!')

        break
    
start()
while True:              
    
    result=end()
    if result=='y':
        start()
    elif result=='n':
        break
        


        
        

