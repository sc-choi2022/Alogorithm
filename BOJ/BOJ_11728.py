import sys

# 배열 A의 크기 N, 배열 B의 크기 M
N, M = map(int, sys.stdin.readline().split())
# 배열 A, B
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.extend(B)
A.sort()
# 두 배열을 합친 후 정렬한 결과를 출력
print(*A)