import sys
from pprint import pprint

# 정점 i를 시작으로 가지는 모든 경로를 확인하는 dfs
def dfs(i):
    # 점정 i에서 j로 가는 모든 경로를 확인하는 for문
    for j in range(N+1):
        # 만약 j가 확인하지 않은 정점이고 j가 i와 연결되어 있어 info[i][j]가 1이라면 정점 j를 매개변수로 dfs 실행
        if j not in visited and info[i][j] == 1:
            visited.append(j)
            dfs(j)

# 정점의 개수 N, 간선의 개수 M
N, M = map(int, sys.stdin.readline().split())

# 연결 정보를 담을 행렬 info
info = [ [0] * (N + 1) for _ in range(N + 1)]

# 주어지는 M개의 정보를 info에 입력하는 for문
for _ in range(M):
    # 양 끝 점 u, v
    u, v = map(int, sys.stdin.readline().split())
    info[u][v] = 1
    info[v][u] = 1
# 확인한 정점을 담을 visited
visited = []
# 출력할 연결 요소의 개수 ans의 값을 0으로 초기화
ans = 0
# N개의 모든 정점에 대한 for문 0번 정점은 없기 때문에 1부터 시작
for i in range(1, N + 1):
    # i가 확인하지 않은 정점일 경우
    if i not in visited:
        # 확인여부를 visited에 추가 후 i를 매개변수로 dfs 실행
        visited.append(i)
        dfs(i)
        # dfs를 마지고 i와 연결된 모든 연결 요소를 확인했으므로 ans 1 증가
        ans += 1
# 연결 요소의 개수 출력
print(ans)