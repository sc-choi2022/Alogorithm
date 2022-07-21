import sys

def w(a, b, c):
    # a <= 0 or b <= 0 or c <= 0인 경우
    if min(a, b, c) <= 0:
        return 1
    # a > 20 or b > 20 or c > 20인 경우
    if max(a, b, c) > 20:
        return w(20, 20, 20)
    # 이미 확인한 a, b, c인 경우
    if dp[a][b][c]:
        return dp[a][b][c]
    # a < b and b < c인 경우
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c-1)
        return dp[a][b][c]
    # 그 외의 경우
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[a][b][c]
# w(a, b, c)가 호출되었다면 값을 dp[a][b][c]에 저장하는 dp
dp = [[[0] * 50 for _ in range(59)] for _ in range(50)]

while True:
    # 정수 a, b, c
    a, b, c = map(int, sys.stdin.readline().split())
    # 마지막 입력 -1, -1, -1인 경우 break
    if (a, b, c) == (-1, -1, -1):
        break
    # w(a, b, c)의 값을 result 변수에 할당
    result = w(a, b, c)
    # 출력
    print(f'w({a}, {b}, {c}) = {result}')