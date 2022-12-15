import sys
# 체스판의 정보를 담을 배열 chess
chess = [list(map(str, sys.stdin.readline().strip())) for _ in range(8)]

# 출력할 개수 ans
ans = 0

for i in range(8):
    for j in range(8):
        # 하얀칸이고 'F'로 위에 말이 있는 경우 ans 1 증가
        if (i + j) % 2 == 0 and chess[i][j] == 'F':
            ans += 1

# ans 출력
print(ans)