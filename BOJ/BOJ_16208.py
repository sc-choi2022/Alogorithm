import sys

# 쇠막대의 수 N
N = int(sys.stdin.readline())
# 쇠막대의 길이를 저장하는 배열 A
A = list(map(int, sys.stdin.readline().split()))
# 최소의 비용 answer
answer = 0
# 첫 쇠막대의 길이 tmp
tmp = sum(A)

for i in range(N-1):
    tmp -= A[i]
    answer += A[i] * tmp

# 필요한 N개의 쇠막대를 얻는 최소의 비용을 출력
print(answer)