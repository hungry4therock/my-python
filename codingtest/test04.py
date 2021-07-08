n= int(input())
x,y=1,1
plans = input().split()

for plans in plans:
    if plan == 'L':
        y -= 1
    if plan == 'R':
        y+=1
    if plan == 'U':
        if x==1:
            continue
        else:
             x -= 1
    if plan == 'D':
        x+=1

print(x,y)