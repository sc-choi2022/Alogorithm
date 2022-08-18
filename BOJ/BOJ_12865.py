# 물건의 수 N, 한도 무게 K
N, K = map(int, input().split())
stuff =[[0, 0] for _ in range(N+1)]
knapsack = [[0 for _ in range(K+1)] for _ in range(N+1)]
for n in range(1, N + 1):
    stuff[n] = list(map(int, input().split()))

for i in range(1, N+1):
    for j in range(1, K+1):
        weight = stuff[i][0]
        value = stuff[i][1]
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value + knapsack[i-1][j-weight], knapsack[i-1][j])

print(knapsack[N][K])