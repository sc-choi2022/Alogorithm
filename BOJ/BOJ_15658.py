import sys

def dfs(idx, numb):
    global maxN, minN
    if idx == N-1:
        maxN = max(maxN, numb)
        minN = min(minN, numb)
        return

    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            if i == 0:
                dfs(idx+1, numb+numbers[idx+1])
            elif i == 1:
                dfs(idx+1, numb-numbers[idx+1])
            elif i == 2:
                dfs(idx+1, numb*numbers[idx+1])
            else:
                dfs(idx+1, numb//numbers[idx+1])
            operator[i] += 1

# 수의 개수 N
N = int(sys.stdin.readline())
# 수를 저장하는 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))
# 사용할 수 있는 연산자의 개수를 저장하는 배열 0:덧셈, 1:뺄셈, 2:곱셈, 3:나눗셈
operator = list(map(int, sys.stdin.readline().split()))

# 최댓값 maxN, 최솟값 minN
maxN, minN = -1e9, 1e9

dfs(0, numbers[0])
print(maxN)
print(minN)