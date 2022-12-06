import sys

# 타로가 지불할 돈
money = int(sys.stdin.readline())
# 잔돈의 종류
coins = [500, 100, 50, 10, 5, 1]

# 잔돈의 개수 cnt
cnt = 0
# 잔돈으로 계산한 후의 남은 잔돈
change = 1000 - money

for i in range(6):
    coin = coins[i]
    cnt += change // coin
    change %= coin

# 잔돈의 개수 출력
print(cnt)