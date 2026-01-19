from collections import defaultdict
import sys

# 카드의 이름 S
S = sys.stdin.readline().rstrip()
cnt = defaultdict(int)

for i in range(0, len(S), 3):
    cnt[S[i:i+3]] += 1

lst = [c for c in cnt.values() if c != 1]

if len(lst):
    print('GRESKA')
else:
    P, K, H, T = 13, 13, 13, 13

    for c in cnt.keys():
        if c[0] == 'P':
            P -= 1
        elif c[0] == 'K':
            K -= 1
        elif c[0] == 'H':
            H -= 1
        elif c[0] == 'T':
            T -= 1
    print(P, K, H, T)