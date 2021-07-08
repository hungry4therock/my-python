#p85

# (1) 단일 list 예
lst = [1,2,3,4,5]
print(lst)
print(type(lst))

for i in lst:
    print(lst[:i])

#p86
# (2) list 색인
x = list(range(1,11))
print(x)
print(x[:5])
print(x[-5:])
print('index 2씩 증가')
print(x[::2])
print(x[1::2])

#p87
# (1) 단일 리스트 객체 생성
a=['a','b','c']
print(a)

# (2) 중첩 리스트 객체 생성
b= [10,20,a,5,True,'문자열']
print(b[0])
print(b[2])
print(b[2][0])
print(b[2][1:])

#p88
# (1) 단일 리스트 객체 생성
num=['one','two','three','four']
print(num)
print(len(num))

# (2) 리스트 원소 추가
num.append('five')
print(num)

# (3) 리스트 원소 삭제
num.remove('five')
print(num)

# (4) 리스트 원소 수정
num[3] = '4'
print(num)

# (5) 리스트 원소 삽입
num.insert(0,'zero')
print(num)

#p89
# (1) 리스트 결합
x = [1,2,3,4]
y = [1.5,2.5]
z = x+y
print(z)

# (2) 리스트 확장
x.extend(y)
print(x)

# (3) 리스트 추가
x.append(y)
print(x)

# (4) 리스트 두 배 확장
lst = [1,2,3,4]
result = lst * 2
print(result)

#P90
# (1) 리스트 정렬
print(result)
result.sort()
print(result)
result.sort(reverse=True)
print(result)

# (2) 리스트 요소 검사
import random
r=[]
for i in range(5):
    r.append(random.randint(1,5))

print(r)
if 4 in r:
    print('있음')
else:
    print('없음')

#p92
# 형식1) 변수 = [실행문 for]
x = [2,4,1,5,7]
# print = (x ** 2)

lst = [i ** 2 for i in x]
print(lst)

# 형식2) 변수 = [실행문 for it]
# 1~10 -> 2의 배수 추출 -> i *2 -> list 저장
num = list(range(1,11))

lst2 = [i*2 for i in num if i % 2 == 0]
print(lst2)




