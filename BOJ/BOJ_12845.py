import sys

# 카드의 개수 N
N = int(sys.stdin.readline())
# 카드의 레벨 L
L = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)

gold = 0
while len(L) > 1:
    # 업그레이드로 합쳐지는 카드 card
    card = L.pop(1)
    gold += L[0] + card

# 받을 수 있는 골드의 최댓값을 출력
print(gold)