import sys

# 퍼즐의 길이 R, C
R, C = map(int, sys.stdin.readline().split())
# 크로스워드 퍼즐
puzzle = [sys.stdin.readline().rstrip() for _ in range(R)]
puzzle_T = list(map(list, zip(*puzzle)))

# 단어를 저장하는 셋 words
words = set()

# 가로의 단어
for i in range(R):
    word = puzzle[i].split('#')
    for w in word:
        if len(w) > 1:
            words.add(w)

# 세로의 단어
for j in range(C):
    word = ''.join(puzzle_T[j]).split('#')
    for w in word:
        if len(w) > 1:
            words.add(w)

# 사전식 순으로 가장 앞서 있는 낱말을 출력
print(list(sorted(words))[0])