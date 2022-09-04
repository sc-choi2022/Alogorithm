import sys
import heapq

# INF을 의미하는 값으로 10억을 설정
INF = int(1e9)
# 학생 수 N, 도로의 개수 M, 마을 번호 XN, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    # 시작점 S, 끝점 E, 도로를 지나는 데 필요한 소요시간 T    S, E, T = map(int, sys.stdin.readline().split())
    graph[S].append((E, T))


def dijkstra(start):
    q = []
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [INF] * (N + 1)
    # 시작 node로 가기 위한 최소시간을 0으로 설정
    # q에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 시간가 짧은 node에 대한 정보 heappop()        dist, now = heapq.heappop(q)

        # 현재 node가 이미 처리된 node라면 continue        if distance[now] < dist:
        continue

        # 현재 node와 연결된 인접한 node 모두 확인
    for i in graph[now]:
        time = dist + i[1]
        # 현재 node를 거치고 node에 도착하는 것이 더 짧은 시간인 경우
        if time < distance[i[0]]:
            distance[i[0]] = time
            heapq.heappush(q, (time, i[0]))
    return distance


ans = 0
for j in range(1, N + 1):
    go = dijkstra(j)
    back = dijkstra(X)
    ans = max(ans, go[X] + back[j])

print(ans)
