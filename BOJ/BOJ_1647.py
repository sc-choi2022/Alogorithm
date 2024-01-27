import sys

def find(N):
    # 노드 N의 부모노드가 자기자신이 아닌 경우
    if parent[N] != N:
        # 최상위 부모노드 탐색
        parent[N] = find(parent[N])
    return parent[N]

def union(a, b):
    # 노드 a와 b의 최상위 노드 탐색
    a, b = find(a), find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 집의 개수 N, 길의 개수 M
N, M = map(int, sys.stdin.readline().split())
# A번 집, B번 집, 유지비 C를 저장하는 배열 edges
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
# 유지비를 기준으로 정렬
edges.sort(key=lambda x:x[2])
# 부모노드를 저장하는 배열 parent
parent = [i for i in range(N+1)]
# 유지비를 저장하는 변수 answer
answer = 0
# edges의 간선 중 연결한 후 가장 마지막 간선의 유지비를 저장하는 변수 last
last = 0
for a, b, c in edges:
    # 사이클이 아닌 경우
    if find(a) != find(b):
        union(a, b)
        answer += c
        last = c
# 남은 길 유지비의 합의 최솟값을 출력
print(answer - last)