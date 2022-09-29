# 늘려야하는 최소고객 수 C, 도시의 개수 N
C, N = map(int, input().split())
INF = 1e9

# 최소 비용을 담을 리스트 minCost를 INF값으로 초기화
minCost = [INF] * (C+100)
# 0명의 고객을 늘어나게 할 수 있는 최소비용을 0으로 저장
minCost[0] = 0

# 주어지는 N개의 정보를 담을 배열 info
info = [list(map(int, input().split())) for _ in range(N)]
# info안의 값 비용과 고객수를 비용을 기준으로 정렬 sortedInfo
sortedInfo = sorted(info, key=lambda x: x[0])

for cost, customer in sortedInfo:
    # i명의 고객을 늘게 할 수 있는 비용을 min값으로 갱신
    for i in range(customer, C+100):
        minCost[i] = min(minCost[i-customer] + cost, minCost[i])

# C명이상의 고객을 늘게 할 수 있는 비용중 가장 작은 값을 출력
print(min(minCost[C:]))