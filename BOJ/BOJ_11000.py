import sys, heapq

# 수업의 개수 N
N = int(sys.stdin.readline())
# 수업의 시작과 끝 정보를 담을 배열 classes
classes = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
classes.sort()

# 힙으로 사용할 배열 room
room = []
# 첫 수업의 끝나는 시간을 room에 heappush
heapq.heappush(room, classes[0][1])

for i in range(1, N):
    # 새로운 강의실이 필요한 경우
    if classes[i][0] < room[0]:
        heapq.heappush(room, classes[i][1])
    # 기존 강의실을 이어서 사용할 수 있는 경우
    else:
        heapq.heappop(room)
        heapq.heappush(room, classes[i][1])
# 사용한 강의실의 가장 마지막 사용종료시간이 담긴 room의 길이를 출력
print(len(room))