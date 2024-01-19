import sys

# 아이스크림의 종류 N, 섞어먹으면 안되는 조합의 개수 M
N, M = map(int, sys.stdin.readline().split())
# 섞으면 안되는 조합을 저장하는 배열 bad
bad = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    b1, b2 = map(int, sys.stdin.readline().split())
    bad[b1][b2], bad[b2][b1] = 1, 1
# 가능한 방법의 개수 answer
answer = 0

for i in range(1, N+1):
    for j in range(i+1, N+1):
        for k in range(j+1, N+1):
            if bad[i][j] + bad[i][k] + bad[j][k] == 0:
                answer += 1
# answer 출력
print(answer)