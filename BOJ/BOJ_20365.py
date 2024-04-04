import sys

def fill():
    R, B = 0, 0
    if problem[0] == 'R':
        R += 1
        tmp = 'R'
    else:
        B += 1
        tmp = 'B'
    for i in range(1, N):
        if problem[i] != problem[i-1]:
            if tmp == 'B':
                tmp = 'R'
                R += 1
            else:
                tmp = 'B'
                B += 1
    return min(B, R) + 1

# 색을 칠해야 하는 문제의 수 N
N = int(sys.stdin.readline())
# 문제 problem
problem = sys.stdin.readline().rstrip()
# 문제를 원하는 색으로 칠할 때까지 필요한 작업 횟수의 최솟값을 출력
print(fill())