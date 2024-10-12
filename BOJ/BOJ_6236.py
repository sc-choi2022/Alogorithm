import sys

# N일 동안 M번 인출하는 정수 N, M
N, M = map(int, sys.stdin.readline().split())
spend = [int(sys.stdin.readline()) for _ in range(N)]
start, end = min(spend), sum(spend)

# 통장에서 인출해야 할 최소 금액 K
K = max(spend)

while start <= end:
    mid = (start+end)//2

    # 출금하여 가진 금액 money, 인출횟수 cnt
    money, cnt = mid, 1

    for s in spend:
        # 인출이 필요한 경우
        if money - s < 0:
            money = mid
            cnt += 1
        money -= s

    if cnt > M or mid < max(spend):
        start = mid+1
    else:
        end = mid-1
        K = mid

print(K)