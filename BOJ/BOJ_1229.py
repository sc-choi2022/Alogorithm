import sys

# 정수 N
N = int(sys.stdin.readline())
numbers = []
i, j = 1, 1

while True:
    if i*j <= N:
        numbers.append(i*j)
        i += 1
        j += 2
    else:
        break

dp = [0]
for i in range(1, N+1):
    tmp = float('inf')
    for j in range(1, len(numbers)):
        if numbers[j] > i:
            break
        tmp = min(tmp, dp[i-numbers[j]]+1)
    dp.append(tmp)

print(dp[-1])
