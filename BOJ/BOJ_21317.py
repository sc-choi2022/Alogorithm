import sys

# 돌의 개수 N
N = int(sys.stdin.readline())
# 작은 점프와 큰 점프에 소모되는 에너지를 저장하는 배열 stones
stones = [(0, 0)] + [tuple(map(int, sys.stdin.readline().split())) for _ in range(N-1)]
# 매우 큰 점프에 필요한 에너지 K
K = int(sys.stdin.readline())

if N == 1:
    print(0)
elif N == 2:
    print(stones[1][0])
elif N == 3:
    print(min(stones[1][0]+stones[2][0], stones[1][1]))
else:
    dp0, dp1 = [0] * (N+1), [0] * (N+1)
    dp0[2] = stones[1][0]

    for i in range(3, N+1):
        dp0[i] += min(dp0[i-1]+stones[i-1][0], dp0[i-2]+stones[i-2][1])

    dp1[4] = K
    for j in range(5, N+1):
        if j == 5:
            dp1[j] += min(dp1[j-1]+stones[j-1][0], dp0[j-3]+K)
        else:
            dp1[j] += min(dp1[j-1]+stones[j-1][0], dp1[j-2]+stones[j-2][1], dp0[j-3]+K)
    print(min(dp0[N], dp1[N]))