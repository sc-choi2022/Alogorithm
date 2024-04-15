from heapq import heappush, heappop
import sys

N = int(sys.stdin.readline())

schedules = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

rooms = []

for start, end in schedules:
    if rooms and rooms[0] <= start:
        heappop(rooms)
    heappush(rooms, end)

print(len(rooms))