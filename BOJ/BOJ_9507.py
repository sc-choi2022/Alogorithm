import sys

# 꿍만의 피보나치 함수 koong
def koong(N):
    # 이미 koong(N)이 계산 된 경우 dp[N] 리턴
    if dp[N]:
        return dp[N]
    # 꿍의 피보나치 함수
    dp[N] = koong(N-1) + koong(N-2) + koong(N-3) + koong(N-4)
    return dp[N]
# 꿍의 피보나치 수를 저장하는 배열 dp
dp = [1, 1, 2, 4] + [0]*64

# 테스트케이스 개수 T
T = int(sys.stdin.readline())

for _ in range(T):
    # 꿍만의 피보나치 함수 N
    N = int(sys.stdin.readline())
    # 꿍 피보나치값을 출력
    print(koong(N))