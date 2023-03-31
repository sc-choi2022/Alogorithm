import sys, heapq

# 크레인의 개수 N
N = int(sys.stdin.readline())
# 크레인의 무게 제한
cranes = list(map(int, sys.stdin.readline().split()))
cranes.sort(reverse=True)
# 박스의 수 M
M = int(sys.stdin.readline())
# 박스의 무게
boxes = list(map(int, sys.stdin.readline().split()))
boxes.sort(reverse=True)

# 모든 박스를 배로 옮기는데 드는 시간의 최솟값 time
time = 0
# 모든 박스를 배로 옮길 수 없는 경우
if boxes[0] > cranes[0]:
    time = -1
else:
    while boxes:
        for crane in cranes:
            for box in boxes:
                if crane >= box:
                    boxes.remove(box)
                    break
        time += 1
# 첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력
print(time)

# heapq 활용
import heapq
n = int(input())
crane = list(map(int, input().split()))
m = int(input())
box = list(map(int, input().split()))
crane.sort(reverse=True)
box.sort(reverse=True)

i = 0
min_heap = []

for x in box:
    while n > i and crane[i] >= x:
        heapq.heappush(min_heap, [0, crane[i]])
        i += 1
    if not min_heap:
        break

    count, c = heapq.heappop(min_heap)
    count += 1
    heapq.heappush(min_heap, [count, c])

if min_heap:
    min_heap.sort(key=lambda x: -x[0])
    print(min_heap[0][0])
else:
    print(-1)