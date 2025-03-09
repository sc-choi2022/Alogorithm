import sys

# N각형 정수 N
N = int(sys.stdin.readline())

# 교차점의 개수를 출력
print(int(N*(N-1)*(N-2)*(N-3)/24))