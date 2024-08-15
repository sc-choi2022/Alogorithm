import sys

def dfs(idx, total):
    global cnt

    if total < 500:
        return
    if idx == N:
        cnt += 1
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            dfs(idx+1, total+weights[i]-K)
            visit[i] = 0

# 운동 키트의 개수 N, 감소하는 중량 K
N, K = map(int, sys.stdin.readline().split())
# 운동 키트의 중량을 저장하는 배열 weights
weights = list(map(int, sys.stdin.readline().split()))
# 사용한 운동 키트를 확인하는 배열 visit
visit = [0] * N
# 항상 500이상이 되는 경우의 수 cnt
cnt = 0

dfs(0, 500)
# cnt 출력
print(cnt)