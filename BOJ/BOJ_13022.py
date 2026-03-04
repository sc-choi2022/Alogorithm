import sys

# 단어 S
S = sys.stdin.readline().rstrip()

right = 'wolf'
idx = 0

for s in S:
    if s == right[idx]:
        continue