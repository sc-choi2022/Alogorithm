import sys

# 지방의 개수 N
N = int(sys.stdin.readline())

# 지방의 예산 정수
budget = list(map(int, sys.stdin.readline().split()))
# 총 예산 M
M = int(sys.stdin.readline())
# 이분탐색의 기준이 되는 start, end
start, end = 0, max(budget)

while start <= end:
    mid = (start + end) // 2

    # mid을 기준으로 총 예산을 계산하여 저장할 변수 add
    add = 0
    for b in budget:
        # 상한액보다 b가 큰 경우
        if b > mid:
            add += mid
        # 상한액보다 b가 작은 경우
        else:
            add += b

    # add가 예산액을 초과하는 경우
    if add > M:
        end = mid - 1
    else:
        start = mid + 1

# 배정된 예산들 중 최댓값인 정수를 출력
print(end)