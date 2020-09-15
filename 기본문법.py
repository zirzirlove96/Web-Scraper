def say_hello(name,age):
	return f"hello {name} is age {age}"

# f라는 format 함수를 사용하여 인자의 값을 출력할 수 있다,
# 파이썬은 keyword argument라는 규칙이 적용되어 say_hello(age=12,name="nico")가 가능하다.

print(say_hello("nico",12))

days = {
        "name":"nico"}

print(days)
##객체를 선언하여 출력 


days = ["Mon", "Tue", "Wed", "Thur", "Fri"]
#days = ("Mon", "Tue", "Wed", "Thur", "Fri") -> 값 변환을 하고 싶지 않을 때 고정 

for day in days:
        print(day)

import math#수학적인 계산을 할 수 있는 module
from math import ceil,fsum # 특정 함수만 가져오려고 할때 

print(ceil(1.2))

#import는 다른 파일에 정의된 함수 또한 모듈로 사용할 수 있게 한다.
#from calculator import plus
#이런 경우 calculator.py의 plus함수를 사용하는 것이다.
