import sys

# 요일의 수 N, 초기 현금 W
N, W = map(int, sys.stdin.readline().split())
# 일의 바이트 코인 가격을 저장하는 배열 bytecoin
bytecoin = [int(sys.stdin.readline()) for _ in range(N)]

answer = 0

for i in range(1, N):
    if answer == 0:
        if bytecoin[i-1] < bytecoin[i]:
            answer = W//bytecoin[i-1]
            W -= answer*bytecoin[i-1]
    else:
        if bytecoin[i-1] > bytecoin[i]:
            W += answer*bytecoin[i-1]
            answer = 0

if answer:
    W += answer*bytecoin[N-1]

print(answer)