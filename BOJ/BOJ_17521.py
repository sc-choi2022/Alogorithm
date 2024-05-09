import sys

# 요일의 수 N, 초기 현금 W
N, W = map(int, sys.stdin.readline().split())
# 일의 바이트 코인 가격을 저장하는 배열 bytecoin
bytecoin = [int(sys.stdin.readline()) for _ in range(N)]

answer = 0
