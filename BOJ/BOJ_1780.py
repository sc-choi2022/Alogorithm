import sys

def divide(R, C, N):
    current = paper[R][C]

    for i in range(R, R+N):
        for j in range(C, C+N):
            # 종이를 그대로 사용할 수 없는 경우
            if paper[i][j] != current:
                next = N//3
                divide(R, C, next)
                divide(R, C+next, next)
                divide(R, C+2*next, next)
                divide(R+next, C, next)
                divide(R+next, C+next, next)
                divide(R+next, C+2*next, next)
                divide(R+2*next, C, next)
                divide(R+2*next, C+next, next)
                divide(R+2*next, C+2*next, next)
                return

    result[current] += 1
    return

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 종이의 종류를 저장하는 배열 result [0, 1, -1]
result = [0, 0, 0]

divide(0, 0, N)

# -1, 0, 1로만 채워진 종이의 개수 출력
print(result[-1])
print(result[0])
print(result[1])