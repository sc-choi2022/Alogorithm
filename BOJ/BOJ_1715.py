# 시간초과가 되지 않기 위해 heapq를 활용
import heapq

# 숫자 카드 묶음의 개수 N
N = int(input())
# 각 묶음의 카드의 수를 담은 리스트 cards
cards = []
# 비교 횟수를 담을 변수 ans값을 0으로 초기화
ans = 0

# N개의 주어진 값을 heapq.heappush를 사용하여 cards에 값을 추가
for _ in range(N):
    heapq.heappush(cards, int(input()))

# cards의 크기가 1이 될때까지 while문 진행
while len(cards) > 1:
    # heapq.heappop를 활용하여 두개의 값을 출력받아 tmp에 할당
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    # tmp를 ans에 더한다.
    ans += tmp
    # tmp값을 다시 heappush에 추가
    heapq.heappush(cards, tmp)

# 최소 비교 횟수를 출력
print(ans)