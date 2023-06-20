import math, sys

# 로봇의 개수 N
N = int(sys.stdin.readline())
robots = [(0, 0, 0, 0)]*N

for i in range(N):
    # 로봇의 좌표 x, y, 이 로봇을 향해 날아가는 미사일의 속도 v
    x, y, v = map(int, sys.stdin.readline().split())
    robots[i] = (i+1, x, y, math.sqrt(x**2+y**2)/v)
robots.sort(key=lambda x:x[3])

for j in range(N):
    # 로봇이 격추되는 순서를 한 줄에 하나씩 출력
    print(robots[j][0])