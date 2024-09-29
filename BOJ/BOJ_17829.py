import sys

def pooling(size, x, y):
    mid = size//2

    if size == 2:
        answer = [numbers[x][y], numbers[x][y+1], numbers[x+1][y], numbers[x+1][y+1]]
        answer.sort()
        return answer[2]
    tl = pooling(mid, x, y)
    tr = pooling(mid, x, y+mid)
    bl = pooling(mid, x+mid, y)
    br = pooling(mid, x+mid, y+mid)
    answer = [tl, tr, bl, br]
    answer.sort()
    return answer[2]

# 행렬의 크기 N
N = int(sys.stdin.readline())
# 행렬을 저장하는 배열 numbers
numbers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 남은 수 출력
print(pooling(N, 0, 0))