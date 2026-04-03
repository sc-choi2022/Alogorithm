import sys

def solve():
    # 위치를 확인하는 변수 idx
    idx = 0
    # for s in S:
    #     if s == right[idx]:
    #         continue
    #     elif s == right[(idx + 1) % 4]:
    #         idx = (idx + 1) % 4
    #     else:
    #         return 0
    if right[idx] != 'f':
        return 0
    return 1

# 단어 S
S = sys.stdin.readline().rstrip()

right = 'wolf'

# 입력으로 주어진 단어가 올바른 단어인 경우에는 1을, 아니면 0을 출력
print(solve())