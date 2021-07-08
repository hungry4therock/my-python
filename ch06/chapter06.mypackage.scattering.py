#p177
# (1) 평균과 제곱근 모듈 import
from statistics import mean
from math import sqrt

# (2) 산술평균 함수
def Avg(date):
    avg = mean(date)
    return avg

# (3) 분산/표준편차 함수
def var_sd(date):
    avg =Avg(date)
    diff = [(d - avg) ** 2 for d in date]
    var = sum(diff)/(len(date)-1)
    sd =sqrt(var)

    return var, sd