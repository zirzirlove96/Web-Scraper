#객체지향 언어 - DJango(상속, 인스턴스 등)
#하나의 클래스(하나의 설계도)로 여러개의 물품, 코드를 만들 수 있다.

class Car():
    weels=4
    doors=4
    windows=4
    seats=4

    #class안의 함수는 method 그 외는 function이다.
    #생성 method의 첫번 째 argument는 instance이다.
    def start(self):
        print("I start")

    #**kwargs를 사용하여 값을 무제한으로 받아올 수 있다.
    def __init__(self, **kwargs):
        self.weels=4
        self.doors=4
        self.windows=4
        self.seats=4
        self.color = kwargs.get("color","black")#기본값
        self.price = kwargs.get("price", "$20")#인자 값을 가져올 수 있다.


    #클래스에 내장되어 있는 기본 메서드들은 오버라이딩 할 수 있다.
    def __str__(self):
        return f"Car with {self.weels} wheels"

#상속관계
#Car의 모든 메서드와 프로퍼티를 가질 수 있다.
class Convertible(Car):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)#부모의 __init__함수를 사용하기 위해 super()사용
        self.time = kwargs.get("time",10)

    def take_off(self):
        return "taking off"

    #override
    #Car의 __str__함수를 대체했으므로 이 함수가 수행된다.
    def __str__(self):
        return f"Car have not roof"

"""
mini = Car(color="green", price="$40")
mini.start()#method를 호출한 instance를 argument로 사용하기 때문에 self를 써줘야 한다.

#print(dir(Car))#dir 내장 함수를 사용해 클래스가 사용할 수 있는 함수를 가르쳐 준다.
print(mini.color, mini.price)
"""

mini = Convertible(color="blue")#자식 클래스에 인자값을 넣어 부모 클래스의 프로퍼티 값을 지정할 수 있게 한다.
print(mini.color)
