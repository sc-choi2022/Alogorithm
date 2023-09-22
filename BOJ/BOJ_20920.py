import sys

# 단어의 개수 N, 길이의 기준 M
N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    # 단어 word
    word = sys.stdin.readline().rstrip()