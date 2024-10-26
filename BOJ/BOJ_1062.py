import sys

# 단어의 개수 N, 가르칠 수 있는 글자의 개수 K
N, K = map(int, sys.stdin.readline().split())
# 단어를 이루는 알파벳을 저장하는 배열 words
words = []

for _ in range(N):
    word = set(list(sys.stdin.readline().rstrip()[4:-4]))

    for w in ('a', 'c', 'i', 'n', 't'):
        if w in word:
            word.remove(w)
    words.append(word)
words.sort(key=lambda x: len(x))

if K < 5:
    print(0)
else:
    dfs()