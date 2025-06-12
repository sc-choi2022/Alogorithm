import sys

def find(x):
    if money[x] == x:
        return x
    money[x] = find(money[x])
    return money[x]

def union(a, b):
    a, b = find(a), find(b)

    if money[a] < money[b]:
        friends[b] = a
    else:
        friends[a] = b

# 학생 수 N, 친구관계 수 M, 가지고 있는 돈 K
N, M, K = map(int, sys.stdin.readline().split())
# 친구비를 저장하는 배열 money
money = list(map(int, sys.stdin.readline().split()))
# 친구 관계를 저장하는 배열 friends
friends = [[] for _ in range(N+1)]

for _ in range(M):
    a, m = map(int, sys.stdin.readline().split())
    union(a, m)

# 친구로 만드는 최소비용 answer
answer = 1e9