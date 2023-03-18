import sys

# 전깃줄의 개수 N
N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# A의 위치순서대로 정렬
lst.sort(key=lambda x : x[0])
# 전깃줄이 있는 A위치까지의 최대 전깃줄 개수를 담을 배열 dp
dp = [0] * N

for i in range(N):
    for j in range(i):
        # A의 j번째와 연결된 B전기줄의 높이가 A의 i번째와 연결된 B전기줄보다 숫자가 작고 dp의 값이 큰 경우
        if lst[i][1] > lst[j][1] and dp[i] < dp[j]:
            # dp[i]값 갱신
            dp[i] = dp[j]
    # i번째 전깃줄 개수 추가
    dp[i] += 1
# N에서 최대 전깃줄의 개수를 뺀 값을 출력
print(N - max(dp))