#p125
from statistics import mean, variance
from math import sqrt

dataset = [2, 4, 5, 6, 1, 8]

# (1) 산술평균
def Avg(data):
    avg = mean(data)
    return avg

print('산술평균=', Avg(dataset))

# (2) 분산/표준편차
def var_sd(date):
    avg = Avg(date)
    #list 내포
    diff = [(d-avg)**2 for d in date]

    var = sum(diff)/(len(data) - 1)
    sd = sqrt(var)

    return var, sd

# (3) 함수 호출
v, s = var_sd(dataset)
print('분산=', v)
print('표준편차=', s)

#p127
#피타고라스 정리
def pytha(s,t):
    a = s**2 - t**2
    b = 2 * s * t
    c = s**2+t**2
    print("3변의 길이:", a, b, c)

pytha(2,1)

#p127
#단계1: 동전 앞면과 뒷면의 난수 확률분포 함수 정의
def coin(n):
    result = []
    for i in range(n):
        r = rnadom. randint(0, 1)
        if (r == 1):
            result.append(1)
        else:
            result.append(0)
        return result
    print(coin(10))

# 단계 2 :몬테카를로 시뮬레이션 함수 정의
def montacoin(n):
    cnt = 0
    for i in range(n):
        cnt += coin(1)[0]
        result = cnt/n

# 단계 3 :몬테카를로 시뮬레이션 함수 호출
    print(montacoin(10))
    print(montacoin(30))
    print(montacoin(100))
    print(montacoin(1000))
    print(montacoin(10000))



