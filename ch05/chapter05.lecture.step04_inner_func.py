#p134
# (1) 일급 함수
def a():
    print('a 함수')
def b():
        print('b함수')
        return b()
b = a()
b()

# (2)  함수 클로저
data = list(range(1, 100))
def outer_func(data):
    dataset = data
    #inner
    def tot():
        tot_val = sum(dataset)
        return tot_val
    def avg(tot_val):
        avg_val = tot_val /len(dataset)
        return avg_val
    return tot, avg

# 외부 함수 호출: data 생성
tot, avg = outer_func(data)

#내부 함수 호출
tot_val = tot()
print('tot=',tot_val)
avg_val = avg(tot_val)
print('avg=',avg_val)

#P135
from statistics import mean
from math import sqrt

data=[4, 5, 3.5, 2.5, 6.3, 5.5]
# (1) 외부 함수: 산포도 함수
def scattering_func(data):
    dataset=data

    # (2) 내부 함수: 산술평균 반환
    def scattering_func(date):
        avg_val = mean(dataset)
        return avg_val
    # (3) 내부 함수 : 분산 반환
    def var_func(avg):
        diff=[(data-avg)**2 for data in dataset]
        print(sum(diff))
        var_val = sum(diff)/(len(dataset) -1)
        return var_val
    # (4) 내부 함수: 표준편차 반환
    def std_func(var):
        std_val = sqrt(var)
        return var_val
    #함수 클로저 반환
    return avg_func, var_func, std_func
# (5) 내부 함수 호출
print('평균:', avg())
print('분산:', var(avg()))
print('표준편차:', std(var(avg())))

#p137
# (1) 중첩함수 정의
def main_function(num):
    num_val =num
    def getter():
        return num_val
    def setter(value):
        nonlocal num_val
        num_val = value

        return getter,setter
# (2) 외부함수 호출
getter, setter = main_func(100)
# (3) 획득자 호출
print('num=',getter())
# (4) 지정자 획득
setter(200)
print('num=',getter())
# p139
# (1) 래퍼 함수
def wrap(func):
    def decorated():
        print('방가워요!')
        func()
        print('잘가요!')
        return decorated
    # (2) 함수 장식자 적용
    @wrap
    def hello():
        print('hi~',"홍길동")
    # (3) 함수호출
    hello()

#p140
# (1) 재귀함수 정의 :1~n 카운트
 def Counter(n):
    if n == 0:
        return 0
    else:
        Counter(n-1)
# (2) 함수 호출1
print('n=0:', Counter(0))
Counter(5)

#p142
# (1) 재귀함수 정의:1~n 누적합(1+2+3+4+5=15)
def Adder(n):
    if n ==1:
        return
    else:
        result = n + Adder(n-1)
        print(n, end='')
        return result
#(2) 함수 호출1
print('n=1:',Adder(1))
# (3) 함수 호출2
print('\nn=5:',Adder(5))
