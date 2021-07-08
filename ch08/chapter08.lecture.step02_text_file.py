#p218
# (1) 현재 작업디렉터리
import os
print('\현재 경로:', os.getcwd())

# (2) 예외처리
try:
    # (3) 파일 읽기
    ftest1 = open('chapter08/data/ftest.txt', mode= 'w')
    print(ftest1.read())

    # (4) 파일 쓰기
    ftest2 = open('chapter08/data/ftest.txt', mode= 'w')
    print(ftest2.write('my first text~~'))

    # (5) 파일 쓰기 + 내용 추가
    ftest3 = open('chapter08/data/ftest.txt', mode= 'a')
    ftest3.write('\nmy second text ~~~')
except Exception as e:
    print('error 발생:', e)
finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()

#P220
#파일 읽기 관련 함수
try:
    # (1) read(): 전체 텍스트 자료 읽기
    ftest = open('chapter08/data/ftest.txt', mode='r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))

    # (2) readline(): 전체 텍스트 줄 단위 읽기
    ftest = open('chapter08/data/ftest.txt', mode='r')
    lines = ftest.readline()
    print(lines)
    print(type(lines))
    print('문단 수:', len(lines))

    # (3) list -> 문장 추출
    docs = []
    for line in lines:
        print(line.strip())
        docs.append(line.strip())
    print(docs)

    # (4) readline(): 한줄 읽기
    ftest = open('chapter08/data/ftest.txt', mode='r')
    line = ftest.readline()
    print(line)
    print(type(line))

except Exception as e:
    print('error발생:', e)

finally:
    # 파일 객체 닫기
    ftest.close()

