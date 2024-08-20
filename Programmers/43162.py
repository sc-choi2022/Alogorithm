from collections import deque

def solution(n, computers):
    answer = 0
    visit = [0] * n

    for i in range(n):
        if not visit[i]:
            answer += 1
            queue = deque([i])
            visit[i] = 1
            while queue:
                current = queue.popleft()
                for j in range(n):
                    if not visit[j] and computers[current][j]:
                        queue.append(j)
                        visit[j] = 1
    return answer