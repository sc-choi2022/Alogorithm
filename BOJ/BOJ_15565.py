import sys

# 인형의 개수 N, 연속된 인형의 기준 K
N, K = map(int, sys.stdin.readline().split())
# 인형의 정보를 저장하는 배열 dolls
dolls = list(map(int, sys.stdin.readline().split()))

answer = 1e6
left, right = 0, 0

print(-1 if answer == 1e6 else answer)