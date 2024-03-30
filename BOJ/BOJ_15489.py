import sys

# 꼭지점의 위치 R, C, 삼각형 변이 포함하는 숫자의 개수 W
R, C, W = map(int, sys.stdin.readline().split())
# 파스칼 삼각형의 숫자를 저장하는 배열 dp
dp = [[0]*i for i in range(1, R+W)]

# 내부에 있는 수들의 합 answer
answer = 0
for i in range(R+W-1):
    # 꼭지점까지의 차이 dif
    dif = i-R+1
    for j in range(i+1):
        if j == 0 or j == i:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        if 0 <= j-(C-1) <= dif:
            answer += dp[i][j]
# answer 출력
print(answer)