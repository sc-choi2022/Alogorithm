from collections import deque
import sys

N = int(sys.stdin.readline())
visit = [[-1]*(N+1) for _ in range(N+1)]
# 이모티콘의 개수, 클립보드 이모티콘 개수
queue = deque()
queue.append((1, 0))
visit[1][0] = 0

while queue:
    emoji, copied = queue.popleft()

    if visit[emoji][emoji] == -1:
        visit[emoji][emoji] = visit[emoji][copied] + 1
        queue.append((emoji, emoji))
    if emoji + copied <= N and visit[emoji+copied][copied] == -1:
        visit[emoji+copied][copied] = visit[emoji][copied] + 1
        queue.append((emoji+copied, copied))
    if emoji - 1 >= 0 and visit[emoji-1][copied] == -1:
        visit[emoji-1][copied] = visit[emoji][copied] + 1
        queue.append((emoji-1, copied))

answer = -1
for i in range(N+1):
    if visit[N][i] != -1 and (answer == -1 or answer > visit[N][i]):
        answer = visit[N][i]
print(answer)