#ㅔ104
# (1) 입력자료 생성
import random
dataset = []
for i in range(10):
    r = random.randint(1, 100)
    dataset.append(r)
print(dataset)

# (2) 변수 초기화
vmax = vmin = dataset[0]
# (3) 최댓값/최소값 구하기
for i in dataset:
    if vmax < i:
        vmax = i
        if vmin > i:
            vmin = I

# (4) 결과 출력
print('max=', vmax, 'min=', vmin)

#p106
# (1) 오름차순 정렬
dataset = [3, 5, 1, 2, 4]
n = len(dataset)
for i in range(0, n-1):
    for j in range(i+1, n):
        if dataset[i] > dataset[j]:
            tmp = dataset[i]
            dataset[i]=dataset[j]
            dataset[j]=tmp
        print(dataset)
#오타
# (2) 내림차순 정렬
dataset = [3, 5, 1, 2, 4]
n = len(dataset)
for i in range(0, n-1):
    for j in range(i+1, n):
        if dataset[i] < dataset[j]:
         tmp= dataset[i]
         dataset[i] = dataset[j]
         dataset[j] = tmp
    print(dataset)
print(dataset)

#p108
dataset = [5, 10, 18, 22, 35, 55, 75, 103]
value = int(input("검색할 값 입력:"))

low = 0
high = len(dataset)
loc = 0
state = False

while  (low <= high):
    mid = (low+high) //2

    if dataset[mid] > value:
        high = mid -1
    elif dataset[mid] < value:
        low = mid+1
    else:
        loc = mid
        state = True
        break

        if state:
             print('찾는 위치: %d 번째' %(loc + 1))
        else:
             print('찾는 길이 없습니다')