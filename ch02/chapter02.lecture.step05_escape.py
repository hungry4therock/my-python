# (1) escape 문자 적용
print('escape 문자 차단')
print('\n 출력 이스케이프 문자')

# (2) escape 문자 기능 차단
print('\\n 출력 이스케이프 기능 차단1')
print(r'\n 출력 이스케이프 기능 차단2')

# (3) 경로표현 c:\python\test
print('path=', 'c:python\test')
print('path=', 'c:python\\test')
print('path=', r'c:python\test')