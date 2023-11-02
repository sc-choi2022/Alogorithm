import sys

# 수열의 개수 N, 합으로 만드는 수 M
N, M = map(int, sys.stdin.readline().split())
# 수열 A
A = list(map(int, sys.stdin.readline().split()))
start, end = 0, 0
# 경우의 수 answer
answer = 0

while start <= end and end <= N:
    add = sum(A[start:end])
    if add == M:
        answer += 1
        end += 1
    elif add > M:
        start += 1
    else:
        end += 1
# 경우의 수를 출력
print(answer)