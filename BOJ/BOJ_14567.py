from collections import deque
import sys

def sorting():
    return

# 과목의 수 N, 선수 조건의 수 M
N, M = map(int, sys.stdin.readline().split())
# 선수과목의 정보를 저장하는 배열 graph, degree
graph = [[] for _ in range(N)]
degree = [0] * (N)

for _ in range(M):
    # 선수과목의 순서 A, B
    A, B = map(int, sys.stdin.readline().split())
    graph[A-1].append(B-1)
    degree[B-1] += 1

# 결과값 answer
answer = [1] * N
sorting()

# 최소 몇 학기에 이수할 수 있는지를 한 줄에 공백으로 구분하여 출력
print(*answer)