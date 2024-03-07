from collections import deque
import sys

# 상근이의 동기수 N
N = int(sys.stdin.readline())
# 리스트의 길이 M
M = int(sys.stdin.readline())
# 친구 배열 friends
friends = [[] for _ in range(N+1)]
visit = [0]*(N+1)
visit[1] = 1

for _ in range(M):
    # 친구관계 A, B
    A, B = map(int, sys.stdin.readline().split())
    # 친구배열의 친구관계를 저장
    friends[A].append(B)
    friends[B].append(A)

for f in friends[1]:
    visit[f] = 1

queue = deque(friends[1])
while queue:
    current = queue.popleft()
    for friend in friends[current]:
        if not visit[friend]:
            visit[friend] = 1
# 결혼식에 초대하는 동기의 수를 출력
print(sum(visit)-1)