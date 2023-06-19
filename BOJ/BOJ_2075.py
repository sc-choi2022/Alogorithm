from heapq import heappush, heappop
import sys

# 표의 크기 N
N = int(sys.stdin.readline())

# NxN의 큰 순서대로 N개를 저장하는 배열 queue
queue = []

for _ in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        heappush(queue, lst[i])
        # 메모리초과 확인 후 추가된 if문
        if len(queue) > N:
            heappop(queue)
# N번째 큰 수를 출력
print(queue[0])