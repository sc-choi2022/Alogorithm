import sys

word_li = set()
for i in range(1, 14):
    wolf = 'w' * i + 'o' * i + 'l' * i + 'f' * i
    wolf_li.add(wolf)

# 단어 S
S = sys.stdin.readline().rstrip()
flag, idx = True, 0



# 입력으로 주어진 단어가 올바른 단어인 경우에는 1을, 아니면 0을 출력
print(1 if flag else 0)