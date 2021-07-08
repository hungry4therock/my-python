#p129 오류
# (1) 튜플형 가변인수
def Func1(name, *names):
    print(name)
    print(names)

    Func1("홍길동", "이순신", "유관순")

#statistics 모듈 import
from statistics import mean, variance, stdev
# (2) 통계량 구하는 함수
def statis(func, *date):
    if func == 'avg':
        return mean(data)
    elif func == 'var:':
        return variance(data)
    elif func == 'std':
        return stdev(data)
    else:
        return 'TypeError'

#statis 함수 호출
print('var=', statis('avg', 1, 2, 3, 4, 5))
print('var=', statis('var', 1, 2, 3, 4, 5))
print('std=', statis('std', 1, 2, 3, 4, 5))

# (3) 딕트형 가변인수
def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)

# emp_func 함수 호출
emp_func('홍길동', 35, addr='서울시', height=175, weight=65 )

#p131
# (1) 일반 함수
def Adder(x, y):
    add = x + y
    return add
print('add=', Adder(10, 20))

# (2) 람다 함수
print('add=', (lambda x, y:x+y)(10, 20))

#p132
# (1) 지역변수
x = 50
def local_func(x):
    x += 50
    local_func(x)
    print('x=', x)

# (2) 전역 변수
def golbal_func():
    global x
    x += 50

global_func()
print('x=', x)
