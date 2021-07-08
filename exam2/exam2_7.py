"""
날짜:2021-05-13
이름:최현진
내용:파이썬 클래스 상속 연습문제
"""

class Person:
    def __init__(self, name, age):
        self._name = name
        self._age  = age

    def hello(self):
        print('--------')
        print('이름:',self._name)
        print('skdl:',self._age)

class :
    def __init__(self, name, age, school, major):
        super(). __init__(name, age)
        self. _school = school
        self. _major = major

    def hello(self):

        print('학교:',self._school)
        print('이름:',self._major)

class :
    def __init__(self, name, age, school, major, company):
        super(). __init__(name, age,school, major)
        self. _company = company

    def hello(self):

        print('회사:',self._company)
