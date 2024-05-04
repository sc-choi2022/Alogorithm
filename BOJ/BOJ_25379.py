import sys

# 원소의 개수 N
N = int(sys.stdin.readline())
# 배열 A
A = list(map(int, sys.stdin.readline().split()))

# 홀수의 개수 cnt
cnt = 0
# 왼쪽으로 보내는 횟수 left, 오른쪽으로 보내는 횟수 right
left, right = 0, 0

for i in range(N):
    if A[i]%2:
        left += i - cnt
        right += N-i-1 - cnt
        cnt += 1

# 홀수와 짝수가 인접한 경우가 최대 1번 등장하도록 하는 시행의 최소 횟수를 출력
print(min(left, right))