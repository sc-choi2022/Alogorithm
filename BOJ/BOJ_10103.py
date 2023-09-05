import sys

# 라운드의 수 N
N = int(sys.stdin.readline())
# 창영이와 상덕이의 점수 C, S
C, S = 100, 100

for _ in range(N):
    # 각 라운드의 창영이와 상덕이의 주사위 수 c, s
    c, s = map(int, sys.stdin.readline().split())
    # 창영이의 주사위가 더 큰 경우
    if c > s:
        S -= c
    # 상덕이의 주사위가 더 큰 경우
    elif c < s:
        C -= s
# 창영이의 점수
print(C)
# 상덕이의 점수
print(S)