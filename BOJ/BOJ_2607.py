import sys

# 단어의 개수 N
N = int(sys.stdin.readline())
# 첫번째 단어 first
first = list(sys.stdin.readline().rstrip())
answer = 0
for _ in range(N-1):
    compare = first[::]
    word = sys.stdin.readline().rstrip()
    cnt = 0
    for w in word:
        if w in compare:
            compare.remove(w)
        else:
            cnt += 1
    if cnt < 2 and len(compare) > 2:
        answer += 1

print(answer)