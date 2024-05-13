import sys

# 선을 그은 횟수 N
N = int(sys.stdin.readline())
# 두 점의 위치를 저장하는 배열 dots
dots = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dots.sort()

# 길이를 확인하는 범위 start, end
start, end = dots[0]
# 그은 선의 총 길이 answer
answer = 0
for i in range(1,  N):
    # 두 점의 위치 S, E
    S, E = dots[i]
    # 선이 이어지는 경우
    if end > S:
        end = max(end, E)
    # 새로운 선을 시작하는 경우
    else:
        answer += end-start
        start, end = S, E

# 마지막 범위를 더한 그은 선의 총길이 출력
print(answer + end-start)