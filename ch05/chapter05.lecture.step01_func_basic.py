#p116
# (1) builtins 함수
import random

help (len)
dataset = list(range(1, 6))
print(dataset)

print('len=', len(dataset))
print('sum=', sum(dataset))
print('max=', max(dataset))
print('min=', min(dataset))

# (2) import 함수
import statistics
from statistics import variance, stdev

print('평균=', statistics.mean(dataset))
print('중위수=', statistics.median(dataset))
print("표본 분산=", variance(dataset))
print("표본 표준편차=", stdev(dataset))

#p123
# (1) 인수가 없는 함수
def userfunc1():
    print('인수가 없는 함수')
    print('userfunc1')

    userfunc1()

# (2) 인수가 있는 함수
def userfunc2(x, y):
    print('userfunc2')
    z =x + y
    print('z=', z)
userfunc2(10, 20)

# (3) return 있는 함수
def usefunc3(x, y):
    print('userfunc3')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return tot, sub, mul, div
#안됨
# 실인수: 키보드 입력
x = int(input('x입력:'))
y = int(input('y입력:'))

t, s, m , d = usefunc3(x, y)
print('tot=', t)
print('sub=', s)
print('mul', m)
print('div', d)

