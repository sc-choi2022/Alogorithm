import sys

def solve():
    # 위치를 확인하는 변수 idx
    idx = 0
    for s in S:
        if s == right[idx]:
            continue
        elif s == right[(idx + 1) % 4]:
            idx = (idx + 1) % 4
        else:
            return 0
    if right[idx] != 'f':
        return 0
    return 1

# 단어 S
S = sys.stdin.readline().rstrip()

right = 'wolf'

print(solve())