import sys

def square(A, B):
    if B == 1:
        for si in range(N):
            for sj in range(N):
                A[si][sj] %= 1000
        return A

    tmp = square(A, B//2)

    # 제곱 개수가 홀수인 경우
    if B%2:
        return 

# 행렬 A의 크기 N, 제곱하는 수 B
N, B = map(int, sys.stdin.readline().split())
# 행렬 A
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 행렬 A를 제곱한 결과
answer = square(A, B)

for a in answer:
    print(*a)