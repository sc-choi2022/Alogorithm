import sys

# 한 시간당 피로도 A, 처리량 B, 회복력 C, 최대 피로도 M
A, B, C, M = map(int, sys.stdin.readline().split())
# 피로도 fatigue, 일량 work
fatigue, work = 0, 0
# 남은 시간 hour
hour = 24

while hour:
    # 일할 수 있는 경우
    if fatigue + A <= M:
        fatigue += A
        work += B
    # 휴식이 필요한 경우
    else:
        fatigue = 0 if fatigue - C < 0 else fatigue - C
    hour -= 1

# 하루에 번 아웃이 되지 않도록 일을 할 때 최대 얼마나 많은 일을 할 수 있는지 출력
print(work)