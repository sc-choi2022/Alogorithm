import sys

def function(cnt):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if friend[i][k] + friend[k][j] == cnt:
                    friend[i][j] = cnt

def check(cnt):
    for i in range(N):
        num = 0
        for j in range(1, cnt + 1):
            num += friend[i].count(j)
        if num == N-1:
            candidate.append(i+1)

    if candidate:
        return True
    return False

# 회원의 수 N
N = int(sys.stdin.readline())
INF = int(1e9)
friend = [[INF]*N for _ in range(N)]
cnt = 1

while True:
    a, b = map(int, sys.stdin.readline().split())

    if a == -1 and b == -1:
        break
    friend[a-1][b-1] = 1
    friend[b-1][a-1] = 1

candidate = []
flag = check(cnt)

while not flag:
    cnt += 1
    function(cnt)
    flag = check(cnt)

print(cnt, len(candidate))
print(*sorted(candidate))