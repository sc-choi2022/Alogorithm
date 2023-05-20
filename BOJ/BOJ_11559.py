from collections import deque
import sys

def bfs(si, sj):
    queue = deque([(si, sj)])
    color = game[si][sj]
    cnt = 1
    boom = [[] for _ in range(6)]
    boom[sj].append(si)

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < 12 and 0 <= nj < 6 and game[ni][nj] == color and ni not in boom[nj]:
                queue.append((ni, nj))
                cnt += 1
                boom[nj].append((ni))
    if cnt < 4:
        return
    else:
        move(boom)

def move(locations):
    global answer
    for i in range(6):
        location = sorted(locations[i], reverse=True)
        num = len(location)
        for l in location:
            game[l][i] = '.' if l-num < 0 else game[l-num][i]
            game[l-num][i] = ',' if l-num-num < 0 else game[l-num-num][i]
    answer += 1

game = [list(sys.stdin.readline().rstrip()) for _ in range(12)]
answer = 0

flag = True

while flag:
    

print(answer)