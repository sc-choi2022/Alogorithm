from itertools import combinations
import sys

# 모눈종이의 크기 H, W
H, W = map(int, sys.stdin.readline().split())
# 모눈종이의 긴길이와 짧은 길이 L, S
L, S = max(H, W), min(H, W)

# 스티커의 수 N
N = int(sys.stdin.readline())
# 모눈종이에 부착가능한 스티커를 담을 배열 stickers
stickers = []
# 넓이의 최댓값 ans
ans = 0

for _ in range(N):
    # 스티커의 두 길이 A, B
    A, B = map(int, sys.stdin.readline().split())
    # 모눈종이안에 부착가능한 경우 stickers에 (A, B) 추가
    if L >= max(A, B) and S >= min(A, B):
        stickers.append((A, B))
# 두 스티커의 모든 경우 combi
combi = list(combinations(stickers, 2))

for c in combi:
    # 스티커1의 길이 L1, S1, 스티커 2의 길이 L2, S2
    L1, S1 = c[0]
    L2, S2 = c[1]

    # 두 스티커를 모눈종이에 붙일 수 있는 경우
    if L >= max(S1 + S2, max(L1, L2)) and S >= min(S1 + S2, max(L1, L2)) or \
        L >= max(L1 + S2, max(S1, L2)) and S >= min(L1 + S2, max(S1, L2)) or \
        L >= max(S1 + L2, max(L1, S2)) and S >= min(S1 + L2, max(L1, S2)) or \
        L >= max(L1 + L2, max(S1, S2)) and S >= min(L1 + L2, max(S1, S2)) or \
        L >= max(L1 + S2, max(S1, L2)) and S >= min(L1 + S2, max(S1, L2)) or \
        L >= max(S1 + S2, max(L1, L2)) and S >= min(S1 + S2, max(L1, L2)) or \
        L >= max(L1 + L2, max(S1, S2)) and S >= min(L1 + L2, max(S1, S2)) or \
        L >= max(L1 + S2, max(S1, L2)) and S >= min(L1 + S2, max(S1, L2)):
        # ans값을 갱신
        ans = max(ans, L1 * S1 + L2 * S2)
# 두 스티커가 붙여진 넓이의 최댓값을 출력
print(ans)