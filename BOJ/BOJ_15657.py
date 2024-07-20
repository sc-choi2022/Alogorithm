import sys

def dfs(tmp):
    if len(tmp) == M:
        print(*tmp)
        return
    for j in range(N):
        if tmp[-1] <= numbers[j]:
            tmp.append(numbers[j])
            dfs(tmp)
            tmp.pop()

# 주어지는 자연수의 개수 N, 수열이 되는 자연수의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 주어지는 자연수를 정렬하여 저장하는 배열 numbers
numbers = sorted(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    dfs([numbers[i]])