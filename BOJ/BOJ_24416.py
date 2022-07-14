# 피보나치 수 재귀호출
def fib(N):
    if N == 1 or N == 2:
        return 1
    else:
        return fib(N-1) + fib(N-2)
# 피보나치 동적 프로그래밍
def fibonacci(N):
    cnt = 0
    f[1], f[2] = 1, 1
    for i in range(3, N):
        cnt += 1
        f[i] = f[i-1] + f[i-2]
    return cnt
# 주어지는 수 N
N = int(input())

# DP로 사용할 리스트 f
f = [0]*(N+1)
# 함수 fib와 fib2의 실행횟수 출력
print(fib(N), fibonacci(N))