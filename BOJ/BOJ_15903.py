from heapq import heapify, heappush, heappop
import sys

# 카드의 개수 N, 카드 합체 횟수 M
N, M = map(int, sys.stdin.readline().split())
# 카드의 상태를 나타내는 N개의 자연수를 담는 배열 card
card = list(map(int, sys.stdin.readline().split()))
heapify(card)

for _ in range(M):
    card1, card2 = heappop(card), heappop(card)
    heappush(card, card1 + card2)
    heappush(card, card1 + card2)
# 만들 수 있는 가장 작은 점수를 출력
print(sum(card))