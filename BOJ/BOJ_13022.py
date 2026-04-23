import sys

word_li = set()
for i in range(1, 14):
    wolf = 'w' * i + 'o' * i + 'l' * i + 'f' * i
    wolf_li.add(wolf)

# 단어 S
S = sys.stdin.readline().rstrip()
flag, idx = True, 0

while idx < len(S):
    tmp = False

    for word in word_li:
        if idx + len(word) <= len(S) and S[idx:idx+len(word)] == word:
            idx += len(word)
            tmp = True
            break

    if not tmp:
        flag = False
        break

# 입력으로 주어진 단어가 올바른 단어인 경우에는 1을, 아니면 0을 출력
print(1 if flag else 0)