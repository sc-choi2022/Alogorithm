import sys
# 수열을 담을 리스트 fibo
fibo = [0] * 91
# 1, 2번째 수를 저장
fibo[1], fibo[2] = 1, 1
# 주어지는 자연수 N
N = int(sys.stdin.readline())
# 3부터 N까지 규칙에 맞게 fibo[i]값을 저장
for i in range(3, N+1):
    fibo[i] = fibo[i-1] + fibo[i-2]
# fibo[N] 출력
print(fibo[N])