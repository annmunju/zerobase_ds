coor = input("열과 행 입력: ")

x = int(coor[1]) #행
y = ord(coor[0]) - ord('a') + 1 #열

# 8가지 이동 경로
move = [(-2,-1),(-2,1),
        (2, -1),(2,1),
        (1, 2),(1,-2),
        (-1, 2),(-1,-2)]

cnt=0

# 체스판을 넘어가는 경우(0보다 작거나 9보다 크거나)를 제외하고 cnt
for m in move :
    if x+m[0] > 0 and x+m[0] <= 8:
        if y+m[1] > 0 and y+m[1] <= 8:
            cnt+=1

print(cnt)