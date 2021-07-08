"""
날짜:2021/07/28
이름:최현진
내용:파이썬 함수 고급 스코프 교재 p132
"""

def sum(x,y):
tot = 0

for k in range(x,y+1):
    tot += k
    return tot

tot = 0
start=1
end=10

tot = sum(start, end)
print('tot:',tot)
