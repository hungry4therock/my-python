"""
날짜:2021/04/27
이름:최현진
내용: 파이썬 표준입출력 실습 교재 p42
"""

#파이썬 표준 출력
print('hello',end='1')
print('python')

print('010','1234','1111',sep='_')

#파이썬 표준 출력
num=input('숫자입력:')

print('입력한 숫자',num)
print('numtype:',type(num))

#입력받은 문자열을 숫자로 변환
result=int(num)
print('result:',result)
print('result type:',type(result))

#서식문자 출력
print('%d년 %d일 %요일'%(2021,4,27,'화'))

#포맷문자 출력
print('이름:{},나이{},주소{}.format('김유신',23,'김해시'))

