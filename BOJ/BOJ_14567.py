from collections import deque
import sys

def sorting():
    result = []
    queue = deque()

    for i in range(1, N+1):
        if not degree[i]:
            queue.append(i)
            answer[i] = 1

# 과목의 수 N, 선수 조건의 수 M
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    # 선수과목의 순서 A, B
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    degree[B] += 1

answer = [1] * (N+1)
