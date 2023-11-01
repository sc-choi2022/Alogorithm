import sys

# f(n)을 나타내는 정수 a1, a0
a1, a0 = map(int, sys.stdin.readline().split())
# 양의 정수 C
C = int(sys.stdin.readline())
# 양의 정수 n0
n0 = int(sys.stdin.readline())

# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
# 위 정의를 만족하는 경우
if ((C-a1) > 0 and a0/(C-a1) <= n0) or ((C-a1) == 0 and a0 <= n0):
    print(1)
else:
    print(0)