from itertools import combinations
import sys

# 재료의 개수 N
N = int(sys.stdin.readline())
# 신맛과 쓴맛을 저장하는 배열 sour, bitter
sour, bitter = [], []
# 신맛과 쓴맛의 차이가 가장 작은 요리 cuisine
cuisine = float('INF')

for _ in range(N):
    S, B = map(int, sys.stdin.readline().split())
    sour.append(S)
    bitter.append(B)
