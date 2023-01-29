import sys

# 도시의 개수 N
N = int(sys.stdin.readline())
# 도로의 길이 road
road = list(map(int, sys.stdin.readline().split()))
# 주유소의 리터당 가격 oil
oil = list(map(int, sys.stdin.readline().split()))

# 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용 minimum
minimum = 0

# 기준이 되는 기름가격 now
now = oil[0]

for i in range(N - 1):
    if now > oil[i]:
        now = oil[i]
    minimum += road[i] * now
# minimum 출력
print(minimum)