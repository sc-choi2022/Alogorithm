from collections import defaultdict
import sys

# 테스트 케이스의 수 N
N = int(sys.stdin.readline())

alphabet = set(chr(i) for i in range(97, 123))

for _ in range(N):
    # 주어지는 문장 S
    S = sys.stdin.readline().rstrip()

    cnt = defaultdict(int)
    for s in S:
        if s in alphabet:
            cnt[s.lower()] += 1
    print(list(cnt.items()))