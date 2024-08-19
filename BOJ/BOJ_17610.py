import sys

def dfs(L, number):
    if L == K:
        if 0 < number <= S:
            result.add(number)
    else:
        dfs(L+1, number+weights[L])
        dfs(L+1, number-weights[L])
        dfs(L+1, number)

# 추의 개수 K
K = int(sys.stdin.readline())
# 추의 무게를 저장하는 배열 weights
weights = list(sorted(map(int, sys.stdin.readline().split())))
# 주어진 모든 추 무게의 합 S
S = sum(weights)
# 가능한 경우의 수를 저장하는 셋 result
result = set()
dfs(0, 0)

# 양팔 저울을 한번만 이용해서는 측정이 불가능한 경우의 수를 출력
print(S-len(result))