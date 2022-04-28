from collections import defaultdict
import sys
sys.stdin = open('sample_input.txt')

def dijkstra(s):
    # 선택된 지점 집합
    U = {s}
    # 최단 거리를 담을 리스트 distance 마지막 노드까지를 담기 위해 N+1개 생성
    distance = [float('inf')] * (N + 1)
    # distance의 시작 위치의 값은 0
    distance[s] = 0
    # s에서 시작하는 모든 도로의 길이를 각 distance의 각 도착 위치 index에 저장
    for e, w in graph[s]:
        distance[e] = w
    # 모든 정점의 개수만큼 for문을 진행
    for _ in range(N + 1):
        # 거리가 가장 작은 값을 찾기 위해 min_val를 inf로 초기화
        min_val = float('inf')

        for i in range(N + 1):
            # 정점이 U에 포함되어지 않고 distance[i]가 min_val보다 작다면
            if i not in U and min_val > distance[i]:
                # min_val를 distance[i]로 초기화 후
                # i를 U에 추가할 후보 idx로 저장
                min_val = distance[i]
                idx = i
        # 가장 값이 작은 idx를 U에 추가
        U.add(idx)
        # graph 딕션너리의 key가 idx인 e,w에 대한 for문
        for e, w in graph[idx]:
            # idx의 위치에서 e의 위치까지 하는 것이 기존 e위치의 값보다 작다면 변경
            distance[e] = min(distance[e], distance[idx] + w)
    # 모든 for문이 끝나고 마지막 distance의 값을 반환
    return distance[-1]


T = int(input())
for case in range(1, T+1):
    # 마지막 연결 지점 번호 N, 도로의 개수 E
    N, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        # 구간의 시작 s, 구간의 끝 e, 구간의 거리 w
        s, e, w = map(int, input().split())
        # graph 딕셔너리에 s를 key로 (e, w)를 value로 값을 추가
        graph[s].append((e, w))
    # 0번 정점에서 시작하기 때문에 dijkstra(0)
    ans =dijkstra(0)
    # 테스트케이스 번호와 ans를 출력
    print(f'#{case} {ans}')