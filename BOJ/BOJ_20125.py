import sys

def find():
    for fi in range(N):
        for fj in range(N):
            if cookie[fi][fj] == '*':
                return (fi+1, fj)

# 정사각형 판의 한 변 길이 N
N = int(sys.stdin.readline())
cookie = [sys.stdin.readline().rstrip() for i in range(N)]

# 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리의 길이 A, B, C, D, E
A, B, C, D, E = 0, 0, 0, 0, 0
# 심장의 위치 hi, hj
hi, hj = find()

for j in range(hj-1, -1, -1):
    if cookie[hi][j] == '*':
        A += 1
    else:
        break

for jj in range(hj+1, N):
    if cookie[hi][jj] == '*':
        B += 1
    else:
        break
li = hi
while cookie[li][hj] == '*':
    li += 1
    C += 1
C -= 1

for i in range(li, N):
    if cookie[i][hj-1] == '*':
        D += 1
    else:
        break
for ii in range(li, N):
    if cookie[ii][hj+1] == '*':
        E += 1
    else:
        break
# 심장의 위치 출력
print(hi+1, hj+1)
# 허리의 길이 출력
print(A, B, C, D, E)