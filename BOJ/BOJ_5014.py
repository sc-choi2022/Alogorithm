import sys

def bfs():
    global answer
    
    for next in (N+U), (N-D):
        if not visit[next]:
            visit[next] = 1
            dfs(next, cnt+1)

# 건물의 층수 F, 강호의 위치 S층, 스타트링크의 위치 G층, 위로 올라갈 수 있는 층 수 U, 아래로 내려갈 수 있는 층수 D
F, S, G, U, D = map(int, sys.stdin.readline().split())

visit = [0] * 2000000
visit[S] = 1

# 눌러야하는 버튼의 최소값
answer = 1e9

dfs(S, 0)

if answer == 1e9:
    print('use the stairs')
else:
    print(answer)