import sys

# 소수 찾는 기준 N, 지우는 K번째 수
N, K = map(int, sys.stdin.readline().split())
numbers = [1] * (N+1)
# 숫자를 지운 횟수
cnt = 0
for i in range(2, N+2):
    for j in range(i, N+1, i):
        if numbers[j]:
            numbers[j] = 0
            cnt += 1
            if cnt == K:
                print(j)
                exit()