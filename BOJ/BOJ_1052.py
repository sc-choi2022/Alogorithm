import sys

# 물변의 개수 N, 한 번에 옮길 수 있는 물병의 수 K
N, K = map(int, sys.stdin.readline().split())
# 상점에서 구매하는 물병의 개수 cnt
cnt = 0

while bin(N).count('1') > K:
    N += 1
    cnt += 1
# 상점에서 사야하는 물병의 최솟값을 출력
print(cnt)