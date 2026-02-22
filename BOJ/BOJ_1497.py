from itertools import combinations
import sys

def play(number, cnt):
    global answer

    if answer < cnt:
        return 

    for k in range(M):
        if guitar[number][k] == 'Y':
            visit[k] = 1
            cnt += 1
    play(number+1, cnt)

# 기타의 개수 N, 곡의 개수 M
N, M = map(int, sys.stdin.readline().split())

guitar = [[0]*M for _ in range(N)]

for i in range(N):
    name, songs = sys.stdin.readline().rstrip().split()

    for j in range(M):
        if songs[j] == 'Y':
            guitar[i][j] = 1

visit = [0] * M
answer = N