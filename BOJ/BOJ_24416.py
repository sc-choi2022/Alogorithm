# 피보나치 수 재귀호출
def fib(N):
    if N == 1 or N == 2:
        return 1
    else:
        return fib(N-1) + fib(N-2)
# 피보나치 동적 프로그래밍
def fib2(N):
    dp = [0] * (N+1)
    dp[1], dp[2] = 1, 1
    cnt2 = 0
    for i in range(3, N+1):
        cnt2 += 1
        dp[i] = dp[i-1] + dp[i-2]
    return cnt2
# 주어지는 수 N
N = int(input())
# 함수 fib와 fib2의 실행횟수 출력
print(fib(N), fib2(N))