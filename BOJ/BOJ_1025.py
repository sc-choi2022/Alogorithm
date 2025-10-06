import sys

N, M = map(int, sys.stdin.readline().split())
numbers = list(map(int, list(sys.stdin.readline().rstrip())))

answer = -1

pd, qd = [], []

for i in range(1, P+1):
    if P%i == 0:
        pd.append(i)
for j in range(1, Q+1):
    if Q%i == 0:
        qd.append(j)
