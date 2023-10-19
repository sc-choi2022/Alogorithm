from itertools import permutations
import sys

def dfs(numbers, cnt):
    if cnt == K:
        result.add(''.join(map(str, numbers)))
        return
    for i in range(N):
        if not visit[i]:
            numbers.append(cards[i])
            visit[i] = 1
            dfs(numbers, cnt + 1)
            numbers.pop()
            visit[i] = 0

# 카드의 개수 N
N = int(sys.stdin.readline())
# 선택하는 카드의 개수 K
K = int(sys.stdin.readline())
# N개의 카드를 저장하는 배열 cards
cards = [int(sys.stdin.readline()) for _ in range(N)]
visit = [0] * N
# 만들어진 정수를 저장하는 배열 result
result = set()
dfs([], 0)
# 상근이가 만들 수 있는 정수의 개수를 출력
print(len(result))

from itertools import permutations
import sys

# permutation
# 카드의 개수 N
N = int(sys.stdin.readline())
# 선택하는 카드의 개수 K
K = int(sys.stdin.readline())
# N개의 카드를 저장하는 배열 cards
cards = [sys.stdin.readline().rstrip() for _ in range(N)]
# 상근이가 만들 수 있는 정수의 개수를 출력
print(len(set(''.join(i) for i in permutations(cards, K))))