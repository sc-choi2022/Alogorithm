import sys

# 게임을 진행하는 사람 수 A
A = int(sys.stdin.readline())
# 구하고자하는 T번째
T = int(sys.stdin.readline())
# 구하고자하는 구호 N
N = int(sys.stdin.readline())

# 뻔, 데기의 개수
cnt0, cnt1 = 0, 0
# 회차 stage
stage = 0
result = []

while True:
    stage += 1

    for _ in range(2):
        cnt0 += 1
        result.append((cnt0, 0))
        cnt1 += 1
        result.append((cnt1, 1))
    for _ in range(stage+1):
        cnt0 += 1
        result.append((cnt0, 0))
    for _ in range(stage+1):
        cnt1 += 1
        result.append((cnt1, 1))

    if cnt0 >= T:
        print(result.index((T, N))%A)
        break