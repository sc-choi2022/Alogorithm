from collections import deque
import sys

def rotate_word(word1, word2):
    # 기준단어 word1
    word2 = deque(list(word2))

    for _ in range(L):
        word2.rotate(1)
        tmp = ''.join(word2)
        if word1 == tmp:
            return True
    return False

# 단어의 개수 N
N = int(sys.stdin.readline())
# 주어지는 단어 words
words = [sys.stdin.readline().rstrip() for _ in range(N)]
# 동일 단어임을 확인한 여부를 저장하는 배열 check
check = [0] * N
# 서로 다른 단어의 개수 answer
answer = 0

for i in range(N):
    # 기준단어의 길이 L
    L = len(words[i])
    if check[i]:
        continue
    check[i] = 1
    answer += 1
    for j in range(i+1, N):
        if L != len(words[j]):
            continue
        if rotate_word(words[i], words[j]):
            check[j] = 1

# 서로 다른 단어가 몇 개인지 출력
print(answer)