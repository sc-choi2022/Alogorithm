import sys

# 공의 개수 N, 팀의 수 K
N, K = map(int, sys.stdin.readline().split())
# 조건을 만족하는 공의 개수 cnt
cnt = (1+K)/2*K

# 공의 개수가 조건보다 작다면 -1 출력
if cnt > N:
    print(-1)
# N이 cnt보다 큰 경우
else:
    # N-cnt이 K의 배수인 경우
    if (N-cnt) % K == 0:
        print(K-1)
    # K의 배수가 아니라면 공이 많은 바구니부터 채워
    # 공이 가장 작은 바구니에는 공이 추가되지 않아 차이가 K개가 된다.
    else:
        print(K)