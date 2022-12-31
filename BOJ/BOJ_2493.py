import sys

# 탑의 수 N
N = int(sys.stdin.readline())
# 탑들의 높이를 담을 배열 towers
towers = list(map(int, sys.stdin.readline().split()))

for i in range(N - 1, -1, -1):
    for j in range(i - 1, -1, -1):
        if towers[i] >= towers[j]:
            print(j, end=' ')
            break
        if towers[i] < towers[j] and j == 0:
            print(0, end=' ')
            break
    print()
    print(i)