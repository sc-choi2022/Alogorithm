import sys

# 나무의 수 N, 필요한 나무의 길이 M
N, M = map(int, sys.stdin.readline().split())
# M개의 나무의 높이 trees
trees = list(map(int, sys.stdin.readline().split()))
# 이분 탐색을 위한 범위 start, end
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2

    add = 0
    for tree in trees:
        if tree >= mid:
            add += tree - mid

    if add >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)