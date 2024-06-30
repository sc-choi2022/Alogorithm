import sys

def dfs(idx, tmp, goal):
    global difference

    if idx == goal:
        difference = min(difference, abs(int(N)-int(tmp))+L)
        return

    for i in range(10):
        if idx == 0 and i == 0:
            continue
        if not wrong[i]:
            dfs(idx+1, tmp+str(i), goal)

# 이동하려고 하는 채널 N
N = sys.stdin.readline().rstrip()
# 고장난 버튼의 개수 M
M = int(sys.stdin.readline())
L = len(N)

if N == '100':
    print(0)
elif M == 0:
    print(min(L, abs(int(N)-100)))
else:
    numbers = list(map(int, sys.stdin.readline().split()))
    wrong = [0] * 10
    for number in numbers:
        wrong[number] = 1
    check = [0]*L

    for i in range(L):
        if not wrong[int(N[i])]:
            check[i] = 1
    if sum(check) == L:
        print(L)
    else:
        difference = 500001