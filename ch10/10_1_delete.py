"""
날짜:2021/05/20
이름:최현진
내용:파이썬 데이터베이스 sql 실습하기
"""

import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='192.168.10.114',
                     user='828hjchoi',
                     password='1234',
                     db='828hjchoi',
                     charset='utf8')

# sql 실행객체 생성
cur = conn.cursor()
# sql 실행
sql = "Delete from `user1` WHERE `uid`='p101';"
cur.execute(sql)
conn.commit()
# 데이터베이스 종료
print('Delete 완료...')