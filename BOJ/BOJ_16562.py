import sys

def make():
    return 

# 학생 수 N, 친구관계 수 M, 가지고 있는 돈 K
N, M, K = map(int, sys.stdin.readline().split())
# 친구비를 저장하는 배열 money
money = list(map(int, sys.stdin.readline().split()))
# 친구 관계를 저장하는 배열 friends
friends = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

# 친구로 만드는 최소비용 answer
answer = 1e9

visit = [0] * (N+1)
visit[0] = 1