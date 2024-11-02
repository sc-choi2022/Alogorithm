import sys

# 학생의 수 N
N = int(sys.stdin.readline())
# 점수를 저장하는 배열 scores
scores = list(map(int, sys.stdin.readline().split()))
dp = [0] * N

for i in range(1, N):
    for j in range(1, i+2):
        continue

print(dp[-1])