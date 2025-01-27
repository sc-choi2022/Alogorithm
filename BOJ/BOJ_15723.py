import sys
from collections import defaultdict, deque

def bfs(A, B):
    queue = deque([A])

    while queue:
        now = queue.popleft()

        # 명제의 결론에 도달한 경우
        if now == B:
            print('T')
            return

        for next in premise[now]:
            queue.append(next)
    print('F')
    return

# 전제의 개수 N
N = int(sys.stdin.readline())
# 전제의 관계를 저장하는 딕셔너리 premise
premise = defaultdict(list)

for _ in range(N):
    # 전제의 a, b의 관계를 premise에 저장
    a, b = sys.stdin.readline().rstrip().split(' is ')
    premise[a].append(b)

# 결론의 개수 M
M = int(sys.stdin.readline())

for _ in range(M):
    # 주어지는 결론 conclusion의 a1, b1
    a1, b1 = sys.stdin.readline().rstrip().split(' is ')

    bfs(a1, b1)