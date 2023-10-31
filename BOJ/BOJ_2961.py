from itertools import combinations
import sys

# 재료의 개수 N
N = int(sys.stdin.readline())
# 신맛과 쓴맛을 저장하는 배열 flavors
flavors = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 신맛과 쓴맛의 차이가 가장 작은 요리 cuisine
cuisine = float('INF')

for i in range(1, N+1):
    cook = combinations(flavors, i)

    for food in cook:
        # 재료로 만들는 음식의 신맛 sour, 쓴맛 bitter
        sour, bitter = 1, 0

        for j in range(i):
            sour *= food[j][0]
            bitter += food[j][1]
        cuisine = min(cuisine, abs(sour-bitter))

# 신맛과 쓴맛의 차이가 가장 작은 요리의 차이를 출력
print(cuisine)