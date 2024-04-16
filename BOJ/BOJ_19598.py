from heapq import heappush, heappop
import sys

# 회의실의 개수 N
N = int(sys.stdin.readline())
# N개의 회의실의 시작시간과 끝나는 시간을 저장하는 배열 shedules
schedules = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

# 사용하는 회의실을 저장하는 배열
rooms = []
# 시작시간과 끝나는 시간이 빠른 순서
for start, end in schedules:
    # 사용 중인 회의실이 있는 경우이면서 가장 일찍 끝나는 회의실을 사용할 수 있는 회이인 경우
    if rooms and rooms[0] <= start:
        heappop(rooms)
    # 현재 회의의 끝나는 시간을 rooms에 추가
    heappush(rooms, end)

# 사용한 회의실의 개수를 출력
print(len(rooms))