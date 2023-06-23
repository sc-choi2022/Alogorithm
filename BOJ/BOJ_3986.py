import sys

# 단어의 수 N
N = int(sys.stdin.readline())
# 좋은 단어의 개수 cnt
cnt = 0

for _ in range(N):
    # 단어 word
    word = sys.stdin.readline().rstrip()
    stack = []

    for letter in word:
        if stack and stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
    if not stack:
        cnt += 1
# 좋은 단어의 수를 출력
print(cnt)