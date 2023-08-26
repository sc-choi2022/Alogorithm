import sys

# 문자열 string
string = sys.stdin.readline().rstrip()
# 대문자를 저장하는 배열 words
words = []
# 만들어야하는 축약어 goal
goal = 'UCPC'

for s in string:
    if s.isupper():
        words.append(s)

# 'UCPC'를 만든 알파벳을 세는 변수 cnt
cnt = -1

for word in words:
    if goal[cnt+1] == word:
        cnt += 1
    # 가능한 조건이 성립된 경우
    if cnt == 3:
        break
# 가능한 경우 "I love UCPC", 없는 경우 "I hate UCPC"를 출력
print('I love UCPC' if cnt == 3 else 'I hate UCPC')