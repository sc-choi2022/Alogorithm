import sys

def play():
    return 

# 기타의 개수 N, 곡의 개수 M
N, M = map(int, sys.stdin.readline().split())

guitar = [[0]*M for _ in range(N)]

for i in range(N):
    name, songs = sys.stdin.readline().rstrip().split()

    for j in range(M):
        if songs[j] == 'Y':
            guitar[i][j] = 1

visit = [0] * M
answer = 0