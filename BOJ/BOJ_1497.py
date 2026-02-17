import sys

def func(idx, cnt, s):
    global answer
    return 

# 기타의 개수 N, 곡의 개수 M
N, M = map(int, sys.stdin.readline().split())

guitar = []
for _ in range(N):
    name, songs = sys.stdin.readline().rstrip().split()
    bi = ''

    for song in songs:
        bi += '1' if song == 'Y' else '0'
    guitar.append((name, int(bi, 2)))

answer = int(1e9)
