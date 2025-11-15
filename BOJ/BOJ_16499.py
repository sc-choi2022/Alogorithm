import sys

# 단어의 개수 N
N = int(sys.stdin.readline())

# 단어들을 저장하는 셋 words
words = set()
for _ in range(N):
    # 단어 word
    word = list(sorted(sys.stdin.readline().rstrip()))
    word = ''.join(word)
    words.add(word)

# 그룹의 최소 개수를 출력
print(len(words))