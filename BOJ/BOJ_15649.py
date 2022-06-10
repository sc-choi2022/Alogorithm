# dfs를 활용한 방법
def dfs(permu):
    # cnt가 M개에 도달하면 permu를 출력 후 return
    if len(permu) == M:
        print(*permu)
        return
    # 1부터 N까지의 숫자에서
    for i in range(1, N+1):
        # permu안에 i가 없다면
        if i not in permu:
            # i를 추가하고
            permu.append(i)
            # permu와 1 증가 시킨 cnt를 넣어 dfs로 보낸다
            dfs(permu)
            # permu에서 i를 제거
            permu.pop()

# 1부터 N까지 M개를 고르기 위해 N, M이 주어진다.
N, M = map(int,input().split())

dfs([])

# permutaions을 활용하는 방법
from itertools import permutations

# 1부터 N까지 M개를 고르기 위해 N, M이 주어진다.
N, M = map(int, input().split())

lst = [ i for i in range(1, N + 1)]
ans = list(permutations(lst, M))

for a in ans:
    print(*a)