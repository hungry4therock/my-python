#p70
# (1) 문자열 열거형객체 이용
string="홍길동"
print(len(string))
for s in string:
    print(s)

# (2) list 열거형객체 이용
lstset = [1,2,3,4,5]

for e in lstset:
    print('원소:',e)

#p72
# (1) range 객체 형성
num1=range(10)
print('num1:',num1)
num2=range(1,10)
print('num2:',num2)
num3=range(1,10,2)
print('num3=',num3)

# (2) range 객체 활용
for n in num1:
    print(n,end='')
print()
for n in num2:
    print(n, end='')
print()
for n in num3:
    print(n,end='')

#p73
# (1) list에 자료 저장
lst=[]
for i in range(10):
    r = random.randint(1,10)
    lst.append(r)

print('lst=',lst)

# (2) list에 자료 참조
for i in range(10):
    print(lst[i]*0.25)

#p74
#구구단 출력: range 함수이용

# (1) 바깥쪽 반복문
for i in range(2,10):
    print('~~~ {}단~~~'.format(i))

    # (2) 안쪽 반복문
    for j in range(1,10):
        print('%d * %d = %d'%(i,j,i*j))

#p75
string=""" 나는 홍길동입니다
주소는 서울시 입니다
나이는 35세입니다"""

sents=[]
words=[]

# (1) 문단 -> 문장
for sen in string.split(sep="\n"):
    sents.append(sen)
    # (2) 문장 -> 단어
    for word in sen.split():
        words.append(word)

print('문장:',sents)
print('문장수:',len(sents))
print('단어:',words)
print('단어수:','len(words)')

