import sys

# 마법사의 수 N
N = int(sys.stdin.readline())
# 마법사의 약속 시간과 도착시간을 저장하는 배열 time
time = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
time.sort(key=lambda x:(x[1]-x[0]))

# 최소인 서로 다른 정수 T의 개수 answer
answer = 0
# 짝수인 경우
if len(time) % 2 == 0:
    # 중앙값 중 작은 값 middle
    middle = len(time) // 2 - 1
    answer = time[middle+1][1] - time[middle+1][0] - (time[middle][1] - time[middle][0]) + 1
else:
    answer = 1
# answer 출력
print(answer)