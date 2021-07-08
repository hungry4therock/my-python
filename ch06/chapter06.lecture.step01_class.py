#p151
# (1) 함수 정의
def cal_func(a,b):
    #변수 선언: 자료 저장
    x = a
    y = b

    def plus():
        p = x+y
        return p

    def minus():
        m = x- y
        return m
    return plus, minus

# (2) 함수 호출
p,m =cal_func(10,20)
print('plus=',p())
print('minus=',m())

# (3) 클래스 정의
class calc_class:
    # 클래스 변수: 자료저장
    x = y = 0

    # 생성자: 객체 생성 +멤버변수 초기화
    def __init__ (self,a,b):
    self. x = a
    self. y = b

    # 클래스 함수
    def plus(self):
        p = self.x + self.y
        return p

    # 클래스 함수
    def minus(self):
        m = self.x - self.y
        return m

# (4) 객체 상성
obj = calc_class(10,20)

# (5) 멤버 호출
print('plus=', obj. plus())
print('minus=', ob. minus())

#p153
class car:
    # (1) 멤버변수
    cc = 0
    door = 0
    carType =None

    # (2) 생성자
    def __init__(self, cc, door, carType):
        # 멤버 변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType

    # (3) 메서드
    def display(self):
        print("자동차는 %d cc이고 문짝은 %d개 타입은 %s"
        %(self.cc, self.door, self.carType))

    # (4) 객체 생성
    car1 = Car(2000, 4, "승용차")
    car2 = Car(3000, 5, "suv")

    # (5) 멤버 호출: object.member()
    car1.display()
    car2.display()

