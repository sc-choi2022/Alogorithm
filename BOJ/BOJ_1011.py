# 테스트 케이스 수 T
T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dp = [0]*(y-x+1)
    dp[1], dp[y-x] = 1, 1

    for i in range(2, y-x):
        if dp[i]:
            continue

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    d = y-x
    n = 0
    while True:
        if d <= n*(n+1):
            break
        n += 1
    if d <= n**2:
        print(n*2-1)
    else:
        print(n*2)