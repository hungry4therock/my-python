#p96
# (1) 중복불가
s = {1,3,5,3,1}
print(len(s))
print(s)

# (2) 요소 반복
for d in s:
    print(d,end='')
print()

# (3) 집합관련 함수
s2 = {3,6}
print(s. union(s2))
print(s. difference(s2))
print(s.intersection(s2))

# (4) 추가,삭제 함수
s3 = {1,3,5}
print(s3)

s3.add(7)
print(s3)

s3.discard(3)
print(s3)

#p98
#중복 원소를 갖는 리스트
gender = ['남','여','남','여']

# 중복 원소 제거
sgender = set(gender)
lgender = list(sgender)
print(lgender)


print(lgender[1])

#p99
# (1) dict 생성 방법1
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic)

# (2) dict 생성 방법2
person = {'name':'홍길동','age':'35','address':'서울시'}
print(person)
print(person['name'])
print(type(dic),type(person))

# (3) 원소 수정, 삭제, 추가
# dict 원소 수정
person['age']=45
print(person)

# dict 원소 삭제
del person['address']
print(person)

#dict 원소 추가
person ['pay']  = 350
print(person)

# p100
# (1) 요소 검사
print(person['age'])
print('age' in person)

# (2) 요소 반복
for key in person.keys():
    print(key)
for v in person.values():
    print(v)
for i in person.items():
    print(i)

# (1) 단어 데이터 셋
charset = ['abc','code','band','band','abd']
wc = {}

# (2) get() 함수 이용 :key 이용 value 가져오기
for key in charset:
    wc[key] = wc.get(key,0) + 1
    print(wc)
    