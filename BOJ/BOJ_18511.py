import sys

def dfs(idx, number):
    global answer
    # 만들어진 수가 자연수의 자릿수-1인 경우
    if idx == L-1:
        if int(number) <= N:
            answer = max(answer, int(number))
    # 만들어진 수가 자연수의 자릿수와 같은 경우 return
    elif idx == L:
        if int(number) <= N:
            answer = max(answer, int(number))
        return
    for i in range(M):
        dfs(idx+1, number+K[i])

# 자연수의 기준 N, 집합 K의 크기 M
N, M = map(int, sys.stdin.readline().split())
# 집합 K
K = sorted(list(sys.stdin.readline().rstrip().split()))
# 자연수 N의 자릿수 L
L = len(str(N))

# N보다 작거나 같은 자연수 중에서, K의 원소로만 구성된 가장 큰 수 answer
answer = 0
dfs(0, '')
# answer 출력
print(answer)