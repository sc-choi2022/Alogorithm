import sys

# 피보나치 수를 저장하는 배열 dp
dp = [0, 1, 2]
# 주어지는 a,b의 범위안에 가능한 피보나치 수를 저장
while dp[-1] <= 10**100:
    dp.append(dp[-1]+dp[-2])

while True:
    # 범위 a, b
    a, b = map(int, sys.stdin.readline().split())
    # 마지막 줄인 경우 break
    if (a, b) == (0, 0):
        break
    # 피보나치 수의 개수 cnt
    cnt = 0

    for i in range(1, len(dp)):
        if a <= dp[i] <= b:
            cnt += 1
        elif dp[i] > b:
            break
    # [a,b]의 피보나치 수의 개수 출력
    print(cnt)