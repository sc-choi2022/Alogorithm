import sys

# 정사각형의 개수 K
K = int(sys.stdin.readline())
# 기준이 되는 2의 제곱 지수 N
N = 0
while True:
    if 2**(N-1) <= K <= 2**N:
        break
    N += 1
# 구매해야하는 가장 작은 초콜릿의 크기 출력
print(2**N, end=' ')

# 쪼개야 하는 최소 횟수 cnt
cnt = -1
while K:
    if K >= 2**N:
        K -= 2**N
    cnt += 1
    N -= 1
# cnt 출력
print(cnt)