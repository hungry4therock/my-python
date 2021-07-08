#p178
# 1. 모듈 추가(방법1)
# 형식) import 패키지명.모듈명
import chapter06. mypackage.scattering

# 데이터 셋
date = [1, 3, 1.5, 2, 1, 3.2]

# 산술평균 함수 호출
print('평균:', chapter06.mypackage.scattering.var_sd(data))
print('분산:', var)
print('표준편차:', sd)

# 2. 모듈 추가(방법2)
# 형식) from.패키지명.모듈명 import 함수명
from chapter06.mypackage.scattering import Avg, var_sd

print('평균:', Avg(data))

var, sd = var_sd(data)
print('분산:', var)
print('표준편차:', sd)

#p180
# (1) 평균과 제곱근 모듈 import
from statistics import mean
from  math import sqrt

# (2) 산술평균 함수
def Avg(data):
    avg = mean(data)
    return avg

# (3) 분산/표준편차 함수
def var_sd(data):
    avg = Avg(data)
    diff = [(d - avg) **2 for d in data]
#리스트 내포
    var = sum(diff)/(len(data)-1)
    sd = sqrt(var)
    return var, sd

# 프로그램 시작점
if __name__ == " __main__":
    data = [1, 3, 5, 7]
    print('평균=', Avg(data))
    var, sd = var_sd()
    print('분산=', var)
    print('표준편차=', sd)

#p181
# (1) 평균과 제곱근 모듈 import
from statistics import mean
from math import sqrt

# (2) 산술평균 함수
def Avg(data):
    avg = mean(data)
    return avg

# (3) 분산/표준편차 함수
def var_sd(data):
    avg = Avg(data)
    diff = [(d - avg)**2 for d in data]
    #list 내포
    var = sum(diff)/(len(data)-1)
    sd = sqrt(var)

    return var, sd

# 프로그램 시작점 없음
data = [1, 3, 5, 7]
print('평균=', Avg(data))
var, sd = var_sd(data)
print('분산=', var)
print('표준편차=', sd)
