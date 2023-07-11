import sys

# 자연수의 개수 N
N = int(sys.stdin.readline())
# 홍준이가 칠판에 적은 수 N개를 저장하는 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))
# 질문의 개수 M
M = int(sys.stdin.readline())
# [S]부터 [E]까지의 펠렌드롬 여부를 dp[S-1][E-1]에 저장하기 위한 배열 dp
dp = [[0]*N for _ in range(N)]

for i in range(N):
    for start in range(N-i):
        end = start + i
        # 펠렌드롬인 경우는 아래와 같은 세 가지 경우가 존재
        # 범위의 글자수가 1개인 경우
        if start == end:
            dp[start][end] = 1
        # 범위의 첫 글자와 마지막 글자가 같은 경우
        elif numbers[start] == numbers[end]:
            # 범위의 글자가 두글자 인 경우
            if start + 1 == end:
                dp[start][end] = 1
            # [start+1]부터 [end-1]범위가 펠린드롬였기에 현재 범위도 펠린드롬인 경우
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1

for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    # 팰린드롬인 경우에는 1, 아닌 경우에는 0을 출력
    print(dp[S-1][E-1])