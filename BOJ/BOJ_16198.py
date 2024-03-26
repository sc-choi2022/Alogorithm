import sys

def dfs(balls, add):
    global answer

    if len(balls) == 2:
        answer = max(answer, add)
        return

    for j in range(1, len(balls)-1):
        tmp = balls.pop(j)
        dfs(balls, add+balls[j-1]*balls[j])
        balls.insert(j, tmp)

# 에너지 구슬의 개수 N
N = int(sys.stdin.readline())
# 에너지 구슬을 저장하는 배열 marbles
marbles = list(map(int, sys.stdin.readline().split()))
# 모을 수 있는 에너지의 최댓값 answer
answer = 0

dfs(marbles, 0)
# 모을 수 있는 에너지의 최댓값을 출력
print(answer)