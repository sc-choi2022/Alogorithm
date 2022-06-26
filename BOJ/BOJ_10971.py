import sys
# 현재의 위치와 이동비용과 방문한 도시를 담은 visited를 매개변수로 dfs 실행
def dfs(now, value, visited):
    global cost
    # N개의 도시를 방문했을 경우
    if len(visited) == N:
        # now위치에서 처음 방문한 도시까지 이동할 수 있다면
        if W[now][visited[0]] != 0:
            # cost와 현재까지 비용 value에 마지막 도시로 가는 비용을 더한 값 중
            # 작은 값을 cost에 할당 후 return
            cost = min(cost, value + W[now][visited[0]])
        return
    # 다음 이동할 도시 선택하기 위한 for문
    for j in range(N):
        # now에서 j로 갈 수 있고 방문하지 않았으며 value가 cost보다 작다면
        if W[now][j] != 0 and j not in visited and cost > value:
            # 방문을 표시하고
            visited.append(j)
            # 방문에 따라 변하는 상황을 담아 dfs 실행
            dfs(j, value + W[now][j], visited)
            # 방문 표시 제거
            visited.pop()

# 도시의 수 N
N = int(sys.stdin.readline())
# 도시의 비용행렬 W
W = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 출력해주 최소비용 cost을 1000000000로 초기화
cost = 1000000000

# 시작위치를 for문으로 정하고 dfs를 시작
for i in range(N):
    dfs(i, 0, [i])
# 모든 방법을 확인하여 최소값을 구하고 cost 출력
print(cost)