import sys

# 교과서의 수 N, 교과서 더미의 수 M
N, M = map(int, sys.stdin.readline().split())

flag = True

for _ in range(M):
    cnt = int(sys.stdin.readline())
    dummy = list(map(int, sys.stdin.readline().split()))

    for i in range(cnt-1):
        if dummy[i] < dummy[i+1]:
            dummy = False
            break
    if not flag:
        break

print('Yes' if flag else 'No')