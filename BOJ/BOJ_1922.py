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

# 컴퓨터의 수 N
N = int(sys.stdin.readline())
# 연결할 수 있는 선의 수 M
M = int(sys.stdin.readline())
# 컴퓨터를 연결하는 데 드는 비용의 정보를 저장하는 배열 edges
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
edges.sort(key=lambda x:x[2])
# 컴퓨터의 상위컴퓨터를 저장하는 배열 parents
parents = [i for i in range(N+1)]
# 모든 컴퓨터를 연결하는데 필요한 최소비용
answer = 0

for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        answer += c
# 모든 컴퓨터를 연결하는데 필요한 최소비용 출력
print(answer)