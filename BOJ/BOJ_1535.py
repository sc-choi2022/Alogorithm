import sys

# 사람의 수 N
N = int(sys.stdin.readline())
# 필요한 체력을 저장하는 배열 L
L = list(map(int, sys.stdin.readline().split()))
# 얻는 기쁨의 크기를 저장하는 배열 J
J = list(map(int, sys.stdin.readline().split()))
dp = [[0]*N for _ in range(N)]