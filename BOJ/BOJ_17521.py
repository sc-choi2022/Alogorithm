import sys

# 요일의 수 N, 초기 현금 W
N, W = map(int, sys.stdin.readline().split())
# N일간 바이트 코인 가격 등락을 저장하는 배열 bytecoin
bytecoin = [int(sys.stdin.readline()) for _ in range(N)]
# 구매한 코인의 개수 buy
buy = 0

for i in range(1, N):
    # 구매한 코인이 없는 경우
    if buy == 0:
        if bytecoin[i-1] < bytecoin[i]:
            buy = W//bytecoin[i-1]
            W %= bytecoin[i-1]
    else:
        # 코인의 매도하는 경우
        if bytecoin[i-1] > bytecoin[i]:
            W += buy*bytecoin[i-1]
            buy = 0

# 모든 코인을 매도할 때 가지고 있는 현금의 최댓값 출력
print(W+buy*bytecoin[N-1] if buy else W)