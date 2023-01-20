import sys

# 지방의 개수 N
N = int(sys.stdin.readline())

# 지방의 예산 정수
budget = list(map(int, sys.stdin.readline().split()))
# 총 예산 M
M = int(sys.stdin.readline())
start, end = 0, max(budget)
ans = 0

while start <= end:
    mid = (start + end) // 2

    add = 0
    for b in budget:
        if mid < b:
            add += mid
        else:
            add += b

    if add <= M:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)