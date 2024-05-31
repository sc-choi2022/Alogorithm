import sys

# N일의 정수 N
N = int(sys.stdin.readline())
# ANA 회사의 주가 stock
stock = list(map(int, sys.stdin.readline().split()))
buy = stock[0]
answer = 0

for i in range(1, N):
    if buy < stock[i]:
        answer = max(answer, stock[i]-buy)
    else:
        buy = stock[i]

# 주식 한 주로 얻을 수 있는 최대 이득을 출력
print(answer)