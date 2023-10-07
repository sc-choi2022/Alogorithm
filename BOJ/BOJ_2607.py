from collections import defaultdict
import sys

def check(word):
    tmp = defaultdict(int)
    for w in word:
        if w not in letter:
            return 0
        tmp[w] += 1
    if abs(sum(list(letter.values())) - sum(list(tmp.values()))) >= 2:
        return 0
    return 1

# 단어의 개수 N
N = int(sys.stdin.readline())
# 첫번째 단어 first
first = sys.stdin.readline().rstrip()
letter = defaultdict(int)
answer = 0
for f in first:
    letter[f] += 1

for _ in range(N-1):
    answer += check(sys.stdin.readline().rstrip())

print(answer)