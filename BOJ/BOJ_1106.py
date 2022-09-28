# 늘려야하는 최소고객 수 C, 도시의 개수 N
C, N = map(int, input().split())
INF = 1e9

minCost = [INF] * (C+100)
minCost[0] = 0

info = [list(map(int, input().split())) for _ in range(N)]
sortedInfo = sorted(info, key=lambda x: x[0])

for cost, customer in sortedInfo:
    for i in range(customer, C+100):
        minCost[i] = min(minCost[i-customer] + cost, minCost[i])

print(min(minCost[C:]))