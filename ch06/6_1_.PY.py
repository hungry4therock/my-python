"""
날짜:2021/07/29
이름:최현진
내용:파이썬 클래스 실습하기 교재 p148
"""

from ch06.sub1.Account import Account
from ch06.sub1.Computer import computer


#객체 생성
kb = Account('국민은행','101-12-1010','김유신',10000)
kb.deposit(40000)
kb.withdraw(7000)
kb.show()

wr= Account('우리은행','101-11-1911','김춘추',30000)
wr.deposit(10000)
wr.withdraw(5000)
wr.show()

#computer 객체 생성
samsung=Computer('삼성',intel i7','16gb','1tb')
imac=Computer('애플',intel i7','32gb','1tb')

samsung.info()
imac.info()
