import sys

# 차의 대수 N
N = int(sys.stdin.readline())
# 입구의 차량 순서
enter = [''] * N
# 출구의 차량 순서
leave = [''] * N
# 추월 차의 대수 cnt
cnt = 0

for i in range(N):
    enter[i] = sys.stdin.readline().rstrip()
for j in range(N):
    leave[j] = sys.stdin.readline().rstrip()
idx = 0

for k in range(N):
    for j in range(idx, N):
        if leave[k] == enter[j]:
            if k-j > 0:
                idx += k-j
                print(idx)