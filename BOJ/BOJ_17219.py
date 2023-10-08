import sys

N, M = map(int, sys.stdin.readline().split())
info = {}

for _ in range(N):
    site, pwd = sys.stdin.readline().split()
    info[site] = pwd

for _ in range(M):
    address = sys.stdin.readline().rstrip()
    print(info[address])