import sys

# 인형의 개수 N, 연속된 개수 K
N, K = map(int, sys.stdin.readline().split())
# 인형을 선호하는 사람의 수 numbers
numbers = list(map(int, sys.stdin.readline().split()))

answer = float('inf')

for i in range(N-K+1):
    for j in range(N-K-i+2):
        T = numbers[i:i+K+j]
        L = len(T)
        M = sum(T)/L
        answer = min(answer, (sum(map(lambda x:(x-M)**2, T))/L)**0.5)

print(answer)