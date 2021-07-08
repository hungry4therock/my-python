"""
날짜:2021/07/30
이름:최현진
내용:파이썬 패키지와 모듈 실습하기 교재 p175
"""

from ch06.sub1.Account import Account
import ch06.sub2.calc
import ch06.sub2.calc as c
from ch06.calc import *

r1 = ch06.calc.plus(1,2)
r2 = c.minus(2,3)
r3 = multi(3,4)
r4 = div(4,2)

print('r1:',r1)
print('r2:',r2)

