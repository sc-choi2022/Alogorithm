from collections import deque
import sys

# 돌의 개수 N
N = int(sys.stdin.readline())
# 돌멩이의 숫자를 저장하는 배열 A
A = list(map(int, sys.stdin.readline().split()))
# 출발점 S
S = int(sys.stdin.readline())

# 돌멩이에 도달 여부를 저장하는 배열 visit
visit = [0] * N

queue = deque([S - 1])
visit[S - 1] = 1

while queue:
    C = queue.popleft()

    for i in (-A[C], A[C]):
        if 0 <= C - i < N and not visit[C - i]:
            visit[C - i] = 1
            queue.append(C - i)

# 방문 가능한 돌들의 개수를 출력
print(sum(visit))