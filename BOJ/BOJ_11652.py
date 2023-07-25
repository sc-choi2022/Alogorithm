from collections import defaultdict
import sys

# 준규가 가지고 있는 숫자 카드의 개수 N
N = int(sys.stdin.readline())
# 카드의 종류와 그 개수를 저장하는 딕셔너리 card
card = defaultdict(int)

for _ in range(N):
    card[int(sys.stdin.readline())] += 1
# 딕셔너리 카드의 배열
lst = list(card.items())
lst.sort(key=lambda x:(-x[1], x[0]))
# 준규가 가장 많이 가지고 있는 정수를 출력
print(lst[0][0])