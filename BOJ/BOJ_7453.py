import sys

# 배열의 크기 N
N = int(sys.stdin.readline())
# 배열 A, B, C, D
A, B, C, D = [0] * N, [0] * N, [0] * N, [0] * N
# 출력할 결과
ans = 0

for i in range(N):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A[i], B[i], C[i], D[i] = a, b, c, d

AB = {}
for a in A:
    for b in B:
        if a + b not in AB:
            AB[a + b] = 1
        else:
            AB[a + b] += 1

for c in C:
    for d in D:
        CD = -1 * (c + d)
        if CD in AB:
            ans += AB[CD]
print(ans)