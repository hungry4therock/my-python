#p224
import os

# 현재 작업 디렉터리 경로 확인
os. getcwd()

# 작업 디렉터리 경로 확인: chapter08 이동
os.chdir('chapter08')
os.getcwd()

# 현재 작업 디렉터리 목록: 리스트 반환
os.listdir('.')

# 디렉터리 생성: 'test' 생성
os.mkdir('test')
os.listdir('.')

# 디렉터리 이동: test 이동
os.chdir('test')
os.getcwd()

#여러 디렉터리 생성: 'test2', 'test03' 생성
os.makedirs('test2/test3')
os.listdir('.')

#

