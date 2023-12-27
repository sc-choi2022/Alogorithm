import sys

def dfs():
    global answer


# 숫자의 개수 N
N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
visit = [0] * N
# 만들 수 있는 올바른 등식의 개수 answer
answer = 0


print(answer)