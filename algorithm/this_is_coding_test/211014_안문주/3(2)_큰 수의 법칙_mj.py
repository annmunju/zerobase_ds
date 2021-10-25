N, M, K = map(int, input("N M K 입력: ").split())
numLs = list(map(int, input("자연수 입력: ").split()))

numLs.sort(reverse=True)
N_1 = numLs[0]; N_2 = numLs[1]

share = M//(K+1)
remain = M%(K+1)

result = (N_1 * K * share) + (N_2 * share) + (N_1 * remain)
print(result)