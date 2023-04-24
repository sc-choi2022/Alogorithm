import sys

# 3x3 배열의 원소를 뒤집는 함수 func
def func(x, y):
    for ii in range(x, x+3):
        for jj in range(y, y+3):
            A[ii][jj] = not A[ii][jj]

# 행렬의 크기 N, M
N, M = map(int, sys.stdin.readline().split())

# 행렬 A, B
A = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

# 연산의 최소횟수 answer
answer = 0

for i in range(N-2):
    for j in range(M-2):
        if A[i][j] != B[i][j]:
            answer += 1
            func(i, j)
# A를 B로 바꿀 수 있는 경우 answer 출력 아닌 경우 -1 출력
print(answer if A == B else -1)