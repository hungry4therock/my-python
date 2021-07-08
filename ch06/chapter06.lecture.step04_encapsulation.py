#p161
class Account:
    # (1) 은닉 멤버변수
    __balance = 0
    __accName = None
    __accNo = None

    # (2) 생성자 :멤버 변수 초기화
    def __init__(self, bal, name, no):
        self. __balance = bal # 잔액 초기화
        self. __accName = name # 예금주
        self. __accNo = no # 계좌 번호

    # (3) 계좌정보 확인: Getter
    def getBalance(self):
        return self. __balance, self. __accName, self. __accNo

    # (4) 입금하기: Setter
    def deposit(self, money):
        if money < 0:
            print('금액 확인')
            return self. __balance += money

    # (5) 출금하기: Setter
    def withdrow(self, money):
        if self.balance < money:
            print('잔액 부족')
            return  self. __balance -= money

# (6) object 생성
acc = Account(1000, '홍길동', '125-152-4125-41')

# (7) Getter 호출
acc. __balance
bal= acc.getBalance()
print('계좌정보:',bal)

# (8) Setter 호출
acc. deposit(10000)
bal = acc.getBalance()
print('계좌 정보:', bal)
