import sys

# A의 원소의 개수 An, B의 원소의 개수 Bn
An, Bn = map(int, sys.stdin.readline().split())
# 집합 A, 집합 B
A = set(map(int, sys.stdin.readline().split()))
B = set(map(int, sys.stdin.readline().split()))

C = A - B
print(len(C))
C = sorted(list(C))
print(*C)