#p102
# (1) 얕은 복사: 주소 복사(내용, 주소동일)
name = ['홍길동','이순신','강감찬']
print('name address =',id(name))

name2 = name
print('name2 address =',id(name2))

print(name)
print(name2)

# 원본 수정
name2[0] = "김길동"
print(name)
print(name2)

# (2) 깊은 복사: 깊은 내용 복사(내용 동일, 주소 다름)
import copy
name3 = copy.deepcopy(name)
print(name)
print(name3)

print('name address=',id(name))
print('name3 address+',id(name3))

#원본 수정
name[1] = "이순신 장군"
print(name)
print(name3)
