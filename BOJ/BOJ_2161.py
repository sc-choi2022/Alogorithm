import sys

# 카드의 개수 N, N개의 카드를 담은 배열 cards
N = int(sys.stdin.readline())
cards = [x for x in range(1, N+1)]

while len(cards):
    print(cards.pop(0), end=' ')
    if not cards:
        break
    cards.append(cards.pop(0))