import sys

def change(target):
    global answer
    if len(S) == len(target):
        # targer이 S인 경우
        if S == target:
            answer = 1
        return
    if target[-1] == 'A':
        change(target[:-1])
    if target[0] == 'B':
        change(target[1:][::-1])

# 문자열 S, T
S = sys.stdin.readline().rstrip()
T = sys.stdin.readline().rstrip()
# S를 T로 바꿀 수 있는 여부를 저장하는 변수 answer
answer = 0

# 문자열 T를 S로 바꾸는 함수 change
change(T)
# answer 출력
print(answer)