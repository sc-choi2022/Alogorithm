import sys

# 원소가 어떤 집합에 속해있는 지 확인하는 함수 find
def find(N):
    if parents[N] != N:
        parents[N] = find(parents[N])
    return parents[N]

# 서로 다른 두 개의 집합을 하나의 집합으로 병합하는 연산 함수 union
def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 행성의 수 N
N = int(sys.stdin.readline())
# 행성의 연결정보를 저장하는 배열 planet
planet = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

parents = [i for i in range(N+1)]
# 간선의 정보를 저장하는 배열 edges
edges = []
# 간선의 정보를 edges에 저장 후 비용을 기준으로 정렬
for i in range(1, N):
    for j in range(i):
        edges.append((i, j, planet[i][j]))
edges.sort(key=lambda x:x[2])

# 모든 행성을 연결했을 때, 최소 플로우의 관리비용 answer
answer = 0

for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c

# 모든 행성을 연결했을 때, 최소 플로우의 관리비용을 출력
print(answer)