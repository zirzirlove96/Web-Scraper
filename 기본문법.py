def say_hello(name,age):
	return f"hello {name} is age {age}"

# f라는 format 함수를 사용하여 인자의 값을 출력할 수 있다,
# 파이썬은 keyword argument라는 규칙이 적용되어 say_hello(age=12,name="nico")가 가능하다.

print(say_hello("nico",12))



