import sys
N = int(sys.stdin.readline())

stack = list()

for n in range(N):
    order = sys.stdin.readline().split()
    leng = len(stack)
    if order[0] == 'push':
        stack.append(order[1])
    elif order[0] == 'pop':
        if leng > 0 :
            print(stack[-1])
            stack.pop()
        else :
            print(-1)
    elif order[0] == 'size':
        print(leng)
    elif order[0] == 'empty':
        if leng == 0 :
            print(1)
        else :
            print(0)
    elif order[0] == 'top':
        if leng > 0:
            print(stack[-1])
        else:
            print(-1)
