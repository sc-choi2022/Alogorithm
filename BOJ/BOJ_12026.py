import sys

# 집의 위치 N
N = int(sys.stdin.readline())
# 보도블럭에 쓰여있는 글자 words
words = sys.stdin.readline().rstrip()
dp = [1000] * N
dp[0] = 0

for i in range(N):
    for j in range(i+1, N):
        if dp[i] != -1:
            if words[i] == 'B' and words[j] == 'O':
                dp[j] = min(dp[j], dp[i] + (j-i)**2)
            elif words[i] == 'O' and words[j] == 'J':
                dp[j] = min(dp[j], dp[i] + (j-i)**2)
            elif words[i] == 'J' and words[j] == 'B':
                dp[j] = min(dp[j], dp[i] + (j-i)**2)

print(dp[-1] if dp[-1] != 1000 else -1)