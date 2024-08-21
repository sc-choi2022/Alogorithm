from collections import deque

def solution(n, computers):
    # 네트워크의 개수 answer
    answer = 0
    # 네트워크에 포함된 컴퓨터를 확인하는 배열 visit
    visit = [0] * n

    for i in range(n):
        # 네트워크에 포함되어 있지 않은 경우
        if not visit[i]:
            answer += 1
            queue = deque([i])
            visit[i] = 1
            while queue:
                current = queue.popleft()
                for j in range(n):
                    # 네트워크에 포함되지 않고 컴퓨터 current와 연결되어 있는 경우
                    if not visit[j] and computers[current][j]:
                        queue.append(j)
                        visit[j] = 1
    return answer