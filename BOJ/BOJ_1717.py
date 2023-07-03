import sys
sys.setrecursionlimit(10**6)

# 루트 노드를 찾는 함수 find
def find(a):
    if a == parent[a]:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]
# a를 포함하는 집합과 b를 포함하는 집합을 합치는 함수 union
def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

# 집합의 개수 N, 연산의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 모든 집합을 포함하는 배열 parent
parent = [x for x in range(N+1)]

for _ in range(M):
    # 연산의 종류 command, 원소 A, 원소 B
    command, A, B = map(int, sys.stdin.readline().split())
    if command == 0:
        union(A, B)
    elif command == 1:
        if find(A) == find(B):
            print('YES')
        else:
            print('NO')