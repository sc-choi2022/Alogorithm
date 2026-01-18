from collections import defaultdict
import sys

# 카드의 이름 S
S = sys.stdin.readline().rstrip()
cnt = defaultdict(int)

for i in range(0, len(S), 3):
    cnt[S[i:i+3]] += 1
