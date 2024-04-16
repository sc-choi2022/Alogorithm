from heapq import heappush, heappop
import sys

# 강의의 개수 N
N = int(sys.stdin.readline())
# 강의의 번호, 시작 시간, 종료 시간을 저장하는 배열 lectures
lectures = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
lectures.sort(key=lambda x: x[1])
# 사용하는 강의실을 사용하는 강의를 저장하는 rooms
rooms = []

for lecture in lectures:
    number, start, end = lecture
    # 사용완료한 강의실을 사용할 수 있는 경우
    if rooms and rooms[0] <= start:
        heappop(rooms)
    heappush(rooms, end)

# 필요한 최소 강의실 개수를 출력
print(len(rooms))