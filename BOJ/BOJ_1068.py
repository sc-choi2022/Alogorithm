import sys

def dfs(idx):
    parents[idx] = -2

    for n in range(N):
        if idx == parents[n]:
            dfs(n)

# 트리의 노드의 개수 N
N = int(sys.stdin.readline())
# 부모노드를 저장한 배열 parents
parents = list(map(int, sys.stdin.readline().split()))
# 지우는 노드의 번호 num
num = int(sys.stdin.readline())

dfs(num)
answer = 0
for i in range(N):
    if parents[i] != -2 and i not in parents:
        answer += 1

print(answer)