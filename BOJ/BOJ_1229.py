import sys

# 정수 N
N = int(sys.stdin.readline())
dp = [0, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 2]
answer = 0

for i in range(2, 7072):
    dp[i] = dp[i-1] + 6*(i-1) - (2*(i-2)+1)

for j in range(7071, -1, -1):
    if N > dp[j]:


print(dp[-1])