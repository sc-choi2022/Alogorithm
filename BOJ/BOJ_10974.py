from itertools import permutations
import sys

# dfs을 활용한 순열
def dfs(visit):
    global N

    if len(visit) == N:
        print(*visit)
        return

    for i in range(1, N+1):
        if i not in visit:
            visit.append(i)
            dfs(visit)
            visit.pop()

# 1부터 N까지의 수로 이루어진 순열의 기준이 되는 N
N = int(sys.stdin.readline())

# permutations을 활용한 순열 P
P = permutations(range(1, N + 1))
# 모든 순열을 출력
for p in P:
    print(*p)

# 빈 배열을 visit으로 함수 dfs 실행
dfs([])