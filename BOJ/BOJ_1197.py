import sys

def find(N):
    if parents[N] != N:
        parents[N] = find(parents[N])
    return parents[N]

# 사이클 여부를 확인하는 함수 union
def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

# 정점의 개수 V와 간선의 개수 E
V, E = map(int, sys.stdin.readline().split())
# 간선의 정보를 저장하는 배열 info
info = [tuple(map(int, sys.stdin.readline().split())) for _ in range(E)]
info.sort(key=lambda x:x[2])

parents = [i for i in range(V+1)]
# 최소 스패닝 트리의 가중치 answer
answer = 0

for a, b, c in info:
    if find(a) != find(b):
        union(a, b)
        answer += c

# 최소 스패닝 트리의 가중치를 출력
print(answer)