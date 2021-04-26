"""
날짜:2021/04/26
이름:최현진
내용: 파이썬 연산자 실습하기 교재 p38
"""

#대입연산자

a=1
b=c=d=0
e,f,g=7,True,'apple'

print('a:',a)
print('c:',c)
print('f:',f)
print('g:',g)

#산출연산자

num1=1
num2=2
num3, num4 = 3, 4

r1= num1+num2
r2= num1-num2
r3= num1*num2
r4= num4/num2
r5= num4//num2
r6= num4%num3 #나머지
r7= num4**num2 #거듭제곱


print('r1:', r1)
print('r2:', r2)
print('r3:', r3)
print('r4:', r4)
print('r5:', r5)

#복합대입연산자

num5, num6, num7, num8 = 5,6,7,8

num5 += 1  #num5=num5+1
num6 -= 2   #num6=num6-2
num7 *= 3 #num7=num7*3
num8 /= 4 #num8=num8/4

#비교연산자

var1=1
var2=2

rs1=var1>var2 # var1이 var2보다 크다
rs2=var1<var2 # var1이 var2보다 작다
rs3=var1>=var2 # var1이 var2보다 크거나 같다
rs4=var1=<var2 # var1이 var2보다 작거나 같다
rs5=var1==var2 # var1이 var2보다 서로 같다
rs6=var1!=var2# var1이 var2보다 서로 다르다

print('rs1:'rs1)
print('rs2:'rs2)
print('rs3:'rs3)
print('rs4:'rs4)

#논리연산자

var3=3
var4=4
res1=(비교식1) and (비교식2)

res1=(var3>2) and (var4>3) #var3는 2보다 크고 그리고 var4는 3보다 크다.
res2=(var3>2) and (var4>4) #var3는 2보다 크고 그리고 var4는 4보다 크다
res3=(var3>2) and (var4>4) #var3는 2보다 크고 또는 var4보다 크다
res4= not (var3>var4) # var3은 var4보다 크지 않다.

print('res1:'res1)
print('res2:'res2)
print('res3:'res3)
print('res4:'res4)