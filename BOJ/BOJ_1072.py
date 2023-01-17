import sys, math

# 게임 횟수 X, 이긴 게임 횟수 Y
X, Y = map(int, sys.stdin.readline().split())

Z = int((Y / X) * 100)

if Z == 100:
    print(-1)
else:
    tmp = Z
    cnt = math.ceil((((Z + 1) / 100) * X - Y) / (1 - (Z + 1)/100))
    print(cnt)