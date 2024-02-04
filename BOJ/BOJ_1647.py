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

# 집의 개수 N, 길의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 집의 부모 노드를 저장하는 배열 parents
parents = [i for i in range(N+1)]
# 길의 정보를 저장하는 배열 edges
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])
# 최소 스패닝 트리에서 제외할 길의 유지비 cost
cost = 0
# 남은 길의 유지비의 합의 최솟값 answer
answer = 0

for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c
        cost = c

# 없애고 남은 길 유지비의 합의 최솟값을 출력
print(answer-cost)