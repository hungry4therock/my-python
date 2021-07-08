"""
날짜:2021/07/28
이름:최현진
내용:파이썬 함수 실습하기 교재 p114

함수(fuction)
-프로그래밍에서 일련의 로직 단위를 모듈로 만든것
-함수는 정의,호출로 이루어진다
"""

#함수 정의:
def f(x):
    y = 2 * x + 3
    return y

#함수호출
r1 = f(1)
r2 = f(2)
r3 = f(3)

print('r1:',r1)
print('r2:',r2)
print('r3:',r3)

#함수 유형1 - 매개변수 0, 리턴값0
def type1(x,y):
    z =  x + y
    return z

rs1= type1(1,2)
rs2= type2(2,3)

print('rs:',rs1)
print('rs2:',rs2)
#함수 유형2 - 매개변수 0, 리턴값x
def type2(items):
    total=0
    for item in items:
        total += item

    print('items 합:',total)

    type2([1, 2, 3, 4, 5])
    type2([2, 4, 6, 8, 10])

#함수 유형3 - 매개변수 x, 리턴값0
def type3():
    total = 0
    for i in range(11):
        total += i

        return total

    result= type3()
    print('result:',result)

#함수 유형4 - 매개변수 x, 리턴값x
def type4():
    print('type3 result:',type3())

type4()
#확인문제
def gugudna(num, '단'):
    for i in range(10):
    print('{} x {}={}'.format(num,i,num*1))

gugudan(2)
gugudan(3)
gugudan(5)


