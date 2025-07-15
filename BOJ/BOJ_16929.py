import sys

def cycle():
    if True:
        return True
    else:
        return False

# 게임판의 크기 N, M
N, M = map(int, sys.stdin.readline().split())
# 게이판의 점의 색을 저장하는 배열 dots
dots = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

if cycle():
    print('Yes')
else:
    print('No')