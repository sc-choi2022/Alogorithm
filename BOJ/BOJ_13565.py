from collections import deque
import sys

def bfs(i):
    global flag
    queue = deque([(0, i)])

    while queue:
        ci, cj = queue.popleft()

        for di, dj in (0, 1), (1, 0), (0, -1), (-1, 0):
            ni,  nj = ci + di, cj + dj
            # (ni, nj)가 섬유 물질 범위에 속하고 전류가 통하는 위치인 경우
            if 0 <= ni < M and 0 <= nj < N and graph[ni][nj] == '0':
                # graph[ni][nj]에 표시, queue에 추가
                graph[ni][nj] = '1'
                queue.append((ni, nj))
                # inner side에 도착한 경우
                if ni == M-1:
                    # 전달 가능여부를 변경 후 break
                    flag = True
                    return

# 격자의 크기 M, N
M, N = map(int, sys.stdin.readline().split())
# 섬유 물질의 2차원 MxN 격자 graph
graph = [list(sys.stdin.readline().rstrip()) for _ in range(M)]
# 전달 가능 여부를 저장하는 변수 flag
flag = False

for i in range(N):
    if graph[0][i] == '0':
        bfs(i)
    # 이미 가능한 경우 break
    if flag:
        break
# flag가 True인 경우 YES 출력
# flag가 False인 경우 NO 출력
print('YES' if flag else 'NO')