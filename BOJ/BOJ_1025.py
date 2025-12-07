import sys

def dfs():
    return 

N, M = map(int, sys.stdin.readline().split())
numbers = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

answer = -1

for i in range(N):
    for j in range(N):
        for row in range(-N, N):
            for col in range(-M, M):
                if row == 0 and col == 0:
                    continue
                step = 0
                x, y = M, N
                val = ''

                while (0 <= x < M) and (0 <= y < N):
                    val += str(numbers[x][y])
                    step += 1

                    val_int = int(''.join(val))
                    val_sqrt = (val_int)**0.5
                    val_deci = val_sqrt - int(val_sqrt)
                    if val_deci == 0 and val_int > answer:
                        answer = val_int
                    x = M + step * row
                    y = N + step * col
print(answer)