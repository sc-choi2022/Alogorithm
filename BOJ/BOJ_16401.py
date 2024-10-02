import sys

# 조카의 수 M와 과자의 수 N
M, N = map(int, sys.stdin.readline().split())
# 과자의 길이를 저장하는 배열 snack
snacks = list(map(int, sys.stdin.readline().split()))
# 이분 탐색의 범위 start, end
start, end = 1, int(1e9)
# 조카 1명에게 줄 수 있는 막대 과자의 최대 길이 answer
answer = 0

while start <= end:
    mid = (start + end)//2
    # 길이 mid로 줄 수 있는 사람의 수 cnt
    cnt = 0

    for snack in snacks:
        cnt += snack//mid

    if cnt >= M:
        answer = max(answer, mid)
        start = mid+1
    else:
        end = mid-1

# answer 출력
print(answer)