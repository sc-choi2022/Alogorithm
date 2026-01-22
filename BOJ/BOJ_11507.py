from collections import defaultdict
import sys

# 카드의 이름 S
S = sys.stdin.readline().rstrip()
# 카드의 개수를 저장하는 딕셔너리 cnt
cnt = defaultdict(int)


# 딕셔너리에 카드의 정보를 저장
for i in range(0, len(S), 3):
    cnt[S[i:i+3]] += 1

# 똑같은 가드가 존재하는 경우를 저장하는 배열 lst
lst = [c for c in cnt.values() if c != 1]

# 똑같은 카드가 존재하는 경우 GRESKA 출력
if len(lst):
    print('GRESKA')
# 그렇지 않은 경우
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
    # P, K, H, T 출력
    print(P, K, H, T)