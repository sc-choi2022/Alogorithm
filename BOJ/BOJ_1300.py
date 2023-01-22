import sys

# NxN 배열의 기준 N
N = int(sys.stdin.readline())
# 인덱스 K
K = int(sys.stdin.readline())
# 이분 탐색을 위한 start, end
start, end = 1, K

while start <= end:
    mid = (start + end) // 2

    tmp = 0
    for i in range(1, N + 1):
        tmp += min(mid//i, N)

    if tmp >= K:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1
print(ans)