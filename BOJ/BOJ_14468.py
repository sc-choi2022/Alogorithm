from collections import defaultdict
import sys

# 주어지는 문자열 S
S = sys.stdin.readline().rstrip()
# 소들의 첫 점을 지난 여부를 저장하는 딕셔너리 cows
cows = defaultdict(int)
stack = []
answer = 0

for s in S:
    cows[s] += 1
    if cows[s] == 1:
        stack.append(s)
    else:
        if stack[-1] == s:
            stack.pop()
        else:
            N = stack.index(s)
            L = len(stack)
            answer += L - N - 1
            stack.pop(N)

print(answer)