from collections import deque
import sys

def bfs(start, end):
    queue = deque([start])
    visit[start] = 0

    while queue:
        num = queue.popleft()

        if num == end:
            return

        for i in range(N):
            if family[num][i] and visit[i] == -1:
                queue.append(i)
                visit[i] = visit[num] + 1

# 전체 사람의 수 N
N = int(sys.stdin.readline())
# 촌수를 계산해야하는 서로 다른 두 사람 A, B
A, B = map(int, sys.stdin.readline().split())

# 각 사람의 촌수를 담을 배열 family
family = [[0]*N for _ in range(N)]
# 부모 자식들 간의 관계의 개수 M
M = int(sys.stdin.readline())
# 확인하여 촌수를 저장할 배열 visit
visit = [-1] * N

for _ in range(M):
    # 부모 자식간의 관계를 family 배열에 저장
    a, b = map(int, sys.stdin.readline().split())
    family[a-1][b-1] = 1
    family[b-1][a-1] = 1

bfs(A-1, B-1)
# 요구한 두 사람의 촌수를 나타내는 정수를 출력, 촌수 계산이 불가능한 경우 -1 출력
print(visit[B-1])