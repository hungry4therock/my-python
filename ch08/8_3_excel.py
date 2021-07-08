"""
날짜:2021/05/03
이름:최현진
내용:파이썬 외부 패키지 설치 교재 p239
"""

from openpyxl import workbook

# excel 파일 쓰기

#엑셀파일 객체 생성
workbook = workbook()

#활성화된 sheet 선택
sheet = workbook.active

# 데이터 입력
sheet['A1'] == '홍길동'
sheet.append([1, 2, 3])
sheet.append(['김유신','김춘추','장보고'])
sheet.cell(6, 2, '사과')

#엑셀 저장/닫기
workbook.save('C:/Users/bigdate/Desktop/test.xlsx')
workbook.close()

print('excel 작업 완료')