from pprint import pprint

# 테스트케이스 T
T = int(input())

for _ in range(T):
    # 소설을 구성하는 장수 K
    K = int(input())
    # 1장부터 K장까지의 파일크기를 담은 리스트 X
    X = [0] + list(map(int, input().split()))

    # dp의 첫값을 넣을 때 필요한 누적합을 담을 리스트 S
    S = [0]*(K+1)
    for i in range(1, K+1):
        S[i] = S[i-1] + X[i]

    # (행)장부터 (열)장까지 합치는 데 필요한 최소비용을 담을 리스트 dp
    dp = [[0]*(K+1) for _ in range(K+1)]

    for i in range(2, K+1):
        for j in range(1, K+2-i):
            dp[j][j+i-1] = min([dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)]) + S[j+i-1] - S[j-1]

    # 1장부터 K장까지 합치는데 필요한 최소비용을 출력한다.
    print(dp[1][K])