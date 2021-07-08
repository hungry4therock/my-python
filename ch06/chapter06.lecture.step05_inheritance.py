# (1) 부모 클래스
class Super:
    # 생성자: 동적 멤버 생성
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # 메서드
        def display(self):
            print('name:%s, age: %d'%(self.name, self.age))
            sup = super('부모',55)
            sup.display()

# (2) 자식 클래스
class sub(Super):
    gender = None

    # (3) 생성자
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # (4) 메서드 확장
    def display(self):
        print('name: %s, age: $d, gender: %s' % (self.name, self.age, self.gender))

sub = sub('자식',25,'여자')
sub.display()

#p168
# (1) 부모 클래스
class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name
    def pay_calc(self):
        pass

# (2) 자식 클래스: 정규직
class Permanent(Employee):
    def __init__(self, name):
        self.name =  name
        super().__init__(name)

    def pay_calc(self, base, bonus):
        print('총수령액:',format(self.pay,'3,d'),'원')

# (3) 자식 클래스: 임시직
class Temporary(Employee):
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time):
        self.pay = tpay * time
        print('총 수령액:',format(self.pay, '3, d')'원')

# (4) 객체 생성
p = Permanent("이순신")
p.pay_calc(3000000, 200000)

t = Temporary("홍길동")
t.pay_calc(15000, 80)

