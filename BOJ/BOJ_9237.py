import sys

# 묘목의 수 N
N = int(sys.stdin.readline())
# 나무가 자라는데 걸리는시간 time
time = list(map(int, sys.stdin.readline().split()))
time.sort(reverse=True)

# 묘목이 다 자라는 날 answer
answer = 0
for i in range(N):
    answer = max(answer, time[i] + i + 1)
# 며칠에 이장님을 초대할 수 있는지 출력
print(answer + 1)