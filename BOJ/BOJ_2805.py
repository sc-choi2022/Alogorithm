import sys

# 나무의 수 N, 필요한 나무의 길이 M
N, M = map(int, sys.stdin.readline().split())
# M개의 나무의 높이 trees
trees = list(map(int, sys.stdin.readline().split()))
# 이분 탐색을 위한 범위 start, end
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2

    # mid 높이에서 구해지는 나무의 길이를 저장할 변수 add
    add = 0
    for tree in trees:
        if tree >= mid:
            add += tree - mid

    if add >= M:
        start = mid + 1
    else:
        end = mid - 1
# 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값을 출력
print(end)