import sys

def KMP(pattern):
    L = len(pattern)
    table = [0 for _ in range(L)]
    pidx = 0
    for idx in range(1, L):
        while pidx > 0 and pattern[pidx] != pattern[idx]:
            pidx = table[pidx-1]

        if pattern[pidx] == pattern[idx]:
            pidx += 1
            table[idx] = pidx
    return table

# 문자열 pattern과 pattern의 길이 P
patterns = sys.stdin.readline()
P = len(patterns)

# 주어진 문자열의 두 번이상 나오는 부분문자열 중에서 가장 긴 길이 answer
answer = 0

for i in range(P):
    answer = max(answer, max(KMP(patterns[i:])))

# answer 출력
print(answer)