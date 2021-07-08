"""
날짜:2021/07/28
이름:최현진
내용:파이썬 함수 고급 실습 교재 p114
"""

#default 매개 변수
def_hello(name='길동',age=21):
print('이름:',name)
print('나이:',age)

hello()
hell0('김유신')
helllo('김춘추',31)

#가변 매개변수
def total(*nums):
    tot = 0
    for n in nums:
        tot += n
        return tot

r1=total(1)
r2=total(1,2)
r3=total(1,2,3)

#하나 이상 리턴 값

def sum_and_multi(num1,num2):
    y1=num1+num2
    y2=num1*num2
    return y1,y2
rs1,rs2=sum_and_multi(1,2)

print('rs1: %d, rs2:%d' % (rs1,rs2))
print('rs3: %d, rs4:%d' % (rs3,rs4))

#변수에 저장하는 함수(익명함수)
def plus(x,y)
    return  x-y

var1 = plus
var2 = minus

res1=var1(1,2)
res2=var2(2,3)

print('res1:',res1)
print('res2:',res2)

cals=[plus,minus]
res3=clas[0](3,4)
res4=clas[1](4,5)

print('res3:',res3)
print('res4:',res4)
#람다함수(익명함수)
lam_plus=lamda x, y : x+y

result=lam_plus(2,3)
print('result:',result)




