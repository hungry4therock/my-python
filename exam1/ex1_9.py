"""
날짜:0000/00/00
이름: 홍길동
내용: 파이썬 선택정렬 연습문제
"""

dataset = [3, 5, 1, 2, 4]
size = len(dataset)

for i in range(size - 1):
    for j in range(i+1, size):
        tmp = dataset[i]
        dataset[i] = dataset[j]
        dataset[j] = tmp

    print('%d round: %s' % (i, dataset))

print('result:', dataset)