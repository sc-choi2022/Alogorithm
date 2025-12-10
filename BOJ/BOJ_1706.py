import sys

# 퍼즐의 길이 R, C
R, C = map(int, sys.stdin.readline().split())
# 크로스워드 퍼즐
puzzle = [list(sys.stdin.readline().rstrip()) for _ in range(R)]

# 단어를 저장하는 셋 words
words = set()

for i in range(R):
    for j in range(C):
        continue