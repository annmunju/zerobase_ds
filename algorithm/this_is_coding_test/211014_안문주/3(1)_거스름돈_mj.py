N = int(input())
print(N)

coinLs = [500, 100, 50, 10]
cntLs = []

for i in coinLs :
    cntLs.append(N//i)
    N %= i

print(cntLs, sum(cntLs))