N, M = map(int, input("N M 입력: ").split())
numLs = []
choiceLs = []

for i in range(N):
    numLs.append(list(map(int, input("자연수 입력: ").split())))

for n in range(N):
    choiceLs.append(min(numLs[n]))

print(max(choiceLs))