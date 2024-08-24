import sys

# 롤케이크의 개수 N과 자를 수 있는 최대 횟수 M
N, M = map(int, sys.stdin.readline().split())
# 롤케이크의 길이를 저장하는 배열 A
A = list(sorted(map(int, sys.stdin.readline().split()), key=lambda x : (x % 10, x)))
cnt = 0
for a in A:
    tmp = a//10
    if not a%10:
        if tmp-1 <= M:
            cnt += tmp
            M -= tmp - 1
        else:
            cnt += M
            M = 0
    else:
        if tmp <= M:
            cnt += tmp
            M -= tmp
        else:
            cnt += M
            M = 0
print(cnt)