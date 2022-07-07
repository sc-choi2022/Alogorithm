import sys

def dfs(x, visited):
    # 이미 확인한 경로
    if dp[x][visited] != 0:
        return dp[x][visited]
    # 모두 방문한 경우
    if visited == (1 << (N - 1)) - 1:
        # 원래 도시로 돌아 올 수 있다.
        if W[x][0]:
            return W[x][0]
        # 원래 도시로 돌아 올 수 없다.
        else:
            return float('inf')
    # 최소값을 float('inf')로 초기화
    min_cost = float('inf')
    # 시작 도시인 1을 제외하고 모든 도시를 방문
    for i in range(1, N):
        # 길이 없거나 이미 방문했다면
        if W[x][i] == 0 or visited & (1 << i-1):
            continue
        # 위 조건으로 경로를 확인하여 비용 계산
        D = W[x][i] + dfs(i, visited | (1 << (i -1)))
        # min_cost와 D 중 작은 값을 min_cost에 할당
        min_cost = min(min_cost, D)
    # dp[x][visited]에 min_cost 할당
    dp[x][visited] = min_cost
    # min_cost return
    return min_cost

# 도시의 수 N
N = int(sys.stdin.readline())

# 비용 행렬 W
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 비용을 담아줄 리스트 dp
dp = [[0]*(1<<N) for _ in range(N)]
# 시작 도시 0과 방문정보 0을 매개변수로 dfs 실행 후 return 값 출력
print(dfs(0, 0))