import sys

A, K = map(int, sys.stdin.readline().split())
# A를 K로 만드는 횟수
cnt = 0

while A != K:
    if K%2 == 0 and K >= 2*A:
        K = K//2
    else:
        K -= 1
    cnt += 1
# 양의 정수 A를 양의 정수 K로 만들기 위해 필요한 최소 연산 횟수를 출력
print(cnt)