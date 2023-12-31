import sys

# 숫자의 개수 N
N = int(sys.stdin.readline())
# 주어지는 숫자를 저장하는 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))
dp = [[0]*21 for _ in range(N-1)]
# 등식의첫번째 숫자의 가능 여부를 저장한다.
dp[0][numbers[0]] = 1

# i번째 숫자까지의 계산 결과로 만들 수 있는 수 j에 표시하는 for문
for i in range(1, N-1):
    for j in range(21):
        # i-1번째 숫자까지의 계산으로 j가 만들어진 경우
        if dp[i-1][j]:
            # 뺄셈의 범위가 음수가 아닌 경우
            if 0 <= j - numbers[i]:
                dp[i][j-numbers[i]] += dp[i-1][j]
            # 덧셈의 범위가 20이하인 경우
            if j + numbers[i] <= 20:
                dp[i][j+numbers[i]] += dp[i-1][j]
# 상근이가 만들 수 있는 올바른 등식의 개수를 출력
print(dp[N-2][numbers[N-1]])