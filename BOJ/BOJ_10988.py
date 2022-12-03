import sys

# 단어 word
word = sys.stdin.readline().strip()

# 팰린드롬인 경우 1 출력
if word == word[::-1]:
    print(1)
# 패린드롬이 아닌 경우 0 출력
else:
    print(0)