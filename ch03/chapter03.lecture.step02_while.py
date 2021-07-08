#p65
# (1) 카운터와 누적변수
cnt=tot=0
while cnt<5:
    cnt+=1
    tot+=cnt
    print(cnt,tot)

# 1~100 사이 3의 배수 합과 원소 추출하기
cnt=tot=0
dateset=[]

while cnt<100:
    cnt+=1
    if cnt % 3 ==0:
        tot+= cnt
        dateset.append(cnt)

print('1~100 사이 3의 배수 합 = %d' % tot)
print('dataset=',dateset)

#p66
#무한 루프
numdate=[]

while True:
    num=int(input("숫자입력:"))

    if num % 10 == 0:
        print("프로그램 종료")
        break
    else:
        print(num)
        numdate.append(num)

#p67
# (1) random module 추가
import random
help(random)

# (2) random 모듈의 함수 도움말
help(random.random)

# (3) 0~1사이 난수 실수
r=random.random()
print('r=', r)

# 난수 0.01미만이면 종료 후 난수 개수 출력
cnt=0
while True:
    r=random.random()
    print(random.random())
    if r < 0.01:
        break
    else:
        cnt += 1
print('난수 개수=',cnt)

#p68
# (1) random 모듈 관련함수 도움말
help(random.randint)
help(random.choices)

# (2) 이름 list에 전체 이름, 특정 이름 출력
names = ['홍길동','이순신','유관순']
print(names)
print(names[2])

# (3) list에서 자료 유무 확인
if '유관순' in names:
    print('유관순 있음')
else:
    print("유관순 없음")

# (4) 난수 정수로 이름 선택
idx= random.randint(0,2)
print(names[idx])

#p69
i=0
while i<10:
    i += 1
    if i ==3:
        continue
    if i ==6:
        break
        print(i, end='')

