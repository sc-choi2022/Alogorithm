def func(N, r, c):
    if N == 0:
        return 0
    return 2*(r%2) + c%2 + 4*func(N-1, int(r//2), int(c//2))

# 정수 N, 행 r, 열 c
N, r, c = map(int, input().split())
print(func(N, r, c))