import sys

# 사람의 수 N
N = int(sys.stdin.readline())

know = [list(sys.stdin.readline().strip()) for _ in range(N)]
visit = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if j == k:
                continue
            if know[j][k] == 'Y' or (know[j][i] == 'Y' and know[i][k] == 'Y'):
                visit[j][k] = 1
result = 0

for v in visit:
    result = max(result, sum(v))

print(result)