from heapq import heappush, heappop
import sys

# 보석의 개수 N, 가방의 개수 K
N, K = map(int, sys.stdin.readline().split())
jewel = []

for _ in range(N):
    heappush(jewel, tuple(map(int, sys.stdin.readline().split())))

# 가방의 허용무게를 담을 리스트 bags
bags = sorted(list(int(sys.stdin.readline()) for _ in range(K)))
# 훔칠 수 있는 보석 가격의 합의 최댓값 answer
answer = 0

# 현재 가방에 넣을 수 있는 보석을 저장하는 배열 values
values = []
for bag in bags:
    # 보석이 남아 있고 가방에 들어가는 보석이 존재할 때
    while jewel and bag >= jewel[0][0]:
        # 보석의 가격을 높은 값부터 정렬하기 위해 음수값으로 가격을 heappush
        heappush(values, -heappop(jewel)[1])
    # 훔칠 수 있는 보석이 있는 경우
    # 가격이 가장 높은 보석을 answer에 더함
    if values:
        answer -= heappop(values)
    # 확인할 보석이 없는 경우 break
    elif not jewel:
        break

# answer 출력
print(answer)