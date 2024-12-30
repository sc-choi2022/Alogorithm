import sys

# 정수 N
N = int(sys.stdin.readline())
# N보다 작은 육각수를 저장하는 배열 numbers
numbers = [0]
i, j = 1, 1

while True:
    if i*j <= N:
        numbers.append(i*j)
        i += 1
        j += 2
    else:
        break

# 합이 index이 되는 육각수 개수의 최솟값을 저장하는 배열 dp
dp = [0] * (N+1)
for di in range(1, N+1):
    tmp = float('inf')
    for dj in range(1, len(numbers)):
        if numbers[dj] > di:
            break
        tmp = min(tmp, dp[di-numbers[dj]]+1)
    dp[di] = tmp

# N을 만들기 위해 필요한 육각수 개수의 최솟값을 출력
print(dp[-1])