"""
날짜:2021/05/03
이름:최현진
내용:파이썬 파일 입출력 실습 교재 p217
"""

#파일 읽기(file input)
file1 = open('C:/Users/bigdate/Desktop/sample.txt', 'r')
line = file1.readline()

print('line:',line)
file1.close()

#여러줄 파일 읽기
file2 = open('C:/Users/bigdate/Desktop/sample.txt', 'r')

while True:
    line = file2.read()

    if not line:
        #읽을 라인이 없을 경우
            break


    print('line:', line)

file2.close()


#파일 쓰기(file output)
file3 = open('C:/Users/bigdate/Desktop/test.txt', 'w')
file3.write('안녕하세요\n')
file3.write('반갑하세요\n')
file3.write('간사합니다\n')
file3.write('간사합니다\n')
file3.close()

#구구단 만들기
file4 = open('C:/Users/bigdate/Desktop/gugudan.txt', 'w')

    file4.write('%단\n' % x)
    for x in range(2,10):
        z = x * y
         print('{} x {} = {}'.format(x, y, z))


file4.close()