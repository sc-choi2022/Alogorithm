# 피보나치 수열을 만드는 함수 fib
def fib(N):
    # N번째 숫자가 구해졌다면 그 수를 return
    if fibo[N]:
        return fibo[N]
    # N번째 숫자를 구할 수 있다면 fibo[N]에 그 수를 할당 후 fibo[N]을 return
    elif fibo[N-1] and fibo[N-2]:
        fibo[N] = fibo[N-1] + fibo[N-2]
        return fibo[N]
    # 그 외의 경우 재귀 활용
    else:
        return fib(N-1) + fib(N-2)

# 45이하의 자연수 N
N = int(input())
# 피보나치 수열을 담을 리스트 fibo
fibo = [0]*46
fibo[1], fibo[2] = 1, 1
# 피보나치 수열의 N번째 값 출력
print(fib(N))