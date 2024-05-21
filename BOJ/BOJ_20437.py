from collections import defaultdict
import sys

# 문자열 게임의 수 T
T = int(sys.stdin.readline())

for _ in range(T):
    cnt = defaultdict(list)
    # 문자열 W
    W = sys.stdin.readline().rstrip()
    # 정수 K
    K = int(sys.stdin.readline())
    # 문자열 W의 길이 L
    L = len(W)
    # 가장 짧은 연속 문자열의 길이 minL, 가장 긴 연속 문자열의 길이 maxL
    minL, maxL = L, 0

    for i in range(L):
        cnt[W[i]].append(i)

    for c in cnt.values():
        # 문자를 K개 이상인 경우
        if len(c) >= K:
            for j in range(len(c)-K+1):
                length = c[j+K-1]-c[j]+1
                minL, maxL = min(minL, length), max(maxL, length)
    # 문자열에 문자를 K개 미만으로 포함한 경우
    if (minL, maxL) == (L, 0):
        print(-1)
    # 3번과 4번에서 구한 연속 문자열의 길이를 공백을 사이에 두고 출력
    else:
        print(minL, maxL)