import sys

def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

# 도시의 수 N
N = int(sys.stdin.readline())
# 여행 계획에 속한 도시들의 수 M
M = int(sys.stdin.readline())

# 도시들의 연결 정보 배열
zido = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 도시의 부모 노드를 저장하는 배열 parent
parent = [x for x in range(N+1)]

# 여행의 계획 plan
plan = list(map(int, sys.stdin.readline().split()))

for i in range(N):
    for j in range(N):
        if zido[i][j] and parent[i+1] != parent[j+1]:
            union(i+1, j+1)
# 방문 첫 도시의 부모 노드
node = find(plan[0])

for k in range(1, M):
    # 방문해야하는 도시가 다른 부모노드를 가지는 경우 NO 출력 후 break
    if find(plan[k]) != node:
        print('NO')
        break
# 도시를 순서대로 방문 가능한 경우 YES 출력
else:
    print('YES')