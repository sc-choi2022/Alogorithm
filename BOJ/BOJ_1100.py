import sys

chess = [list(map(str, sys.stdin.readline().strip())) for _ in range(8)]

# 출력할 개수 ans
ans = 0

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0 and chess[i][j] == 'F':
            ans += 1

# ans 출력
print(ans)