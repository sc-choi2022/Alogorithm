from collections import deque
import sys

def bfs(start, group):
    queue = deque([start])
    visit[start] = group

    while queue:
        tmp = queue.popleft()

        for i in graph[tmp]:
            if not visit[i]:
                queue.append(i)
                visit[i] = -1 * visit[tmp]
            # 연결된 정점끼리는 같은 집합인 경우 False return
            elif visit[i] == visit[tmp]:
                return False
    return True

# 테스트 케이스 개수 K
K = int(sys.stdin.readline())

for _ in range(K):
    # 그래프의 정점의 개수 V와 간선의 개수 E
    V, E = map(int, sys.stdin.readline().split())
    # 간선의 정보를 저장할 배열 graph
    graph = [[] for _ in range(V)]
    # 정점의 확인여부를 저장하는 배경 visit
    visit = [0] * V

    for _ in range(E):
        # 간선의 정보 u, v
        u, v = map(int, sys.stdin.readline().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    for i in range(V):
        if not visit[i]:
            result = bfs(i, 1)
            # 이분 그래프가 아닌 경우 break
            if not result:
                break
    # 주어진 그래프가 이분 그래프이면 YES, 아니면 NO를 순서대로 출력
    print('YES' if result else 'NO')