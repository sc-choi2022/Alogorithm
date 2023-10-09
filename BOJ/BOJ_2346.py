from collections import deque
import sys

# 풍선의 개수 N
N = int(sys.stdin.readline())
# 풍선의 종이를 저장하는 배열
orders = deque(enumerate(map(int, sys.stdin.readline().split())))
# 터진 풍선의 번호를 저장하는 배열 answer
answer = []
while orders:
    idx, paper = orders.popleft()
    answer.append(idx + 1)
    # 종이에 0은 적혀있지 않다.
    # 종이의 값이 양수인 경우
    if paper > 0:
        orders.rotate(-(paper-1))
    # 종이의 값이 음수인 경우
    else:
        orders.rotate(-paper)
# 터진 풍선의 번호를 차례로 나열
print(*answer)