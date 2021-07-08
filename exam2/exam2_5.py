"""
날짜:2021-05-13
이름:최현진
내용:파이썬 클래스 문제
"""

class King:

    def __init__(self, name='태조', year='1392'):
        self.name = name
        self.year = year

    def show(self):
        print('---------')
        print('name:', self.name)
        print('year:', self.year)

if __name__ == '__main__':

    King1 = King()
    King2 = King('태종')
    King3 = King('세종', 1418)

    King1.show()
    King2.show()
    King3.show()
