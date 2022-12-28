import sys

# 요리시간 T초
T = int(sys.stdin.readline())

# 버튼을 누르는 횟수를 저장할 변수 A, B, C
A, B, C = 0, 0, 0

# A를 누르는 경우
if T // 300:
    A += T // 300
    T %= 300
# B를 누르는 경우
if T // 60:
    B += T // 60
    T %= 60
# C를 누르는 경우
if T // 10:
    C += T // 10
    T %= 10
# T초를 맞출 수 없는 경우
if T:
    # -1을 출력
    print(-1)
# T초를 맞출 수 있는 경우
else:
    # A, B, C를 출력
    print(A, B, C)