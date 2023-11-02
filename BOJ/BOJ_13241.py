import sys

# 두 정수 A와 B
A, B = map(int, sys.stdin.readline().split())
# 최소공배수 result의 값을 A*B으로 초기화
result = A*B

while B:
    if A > B:
        A, B = B, A
    B %= A

# A와 B의 최소공배수를 한 줄에 출력
print(result//A)