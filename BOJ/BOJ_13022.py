import sys

# 단어 S
S = sys.stdin.readline().rstrip()

right = 'wolf'
idx = 0

for s in S:
    if s == right[idx]:
        continue
    elif s == right[(idx+1)%4]:
        idx = (idx+1)%4