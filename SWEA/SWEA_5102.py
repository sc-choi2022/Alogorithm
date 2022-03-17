from pprint import pprint
from collections import deque
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T+1):
    # 노드의 개수 V 간선의 개수 E
    V, E = map(int, input().split())
    # 노드와 간선의 정보를 담을 리스트 arr를 index를 잘 맞추기 위해 행과 열을 1씩 키워서 만든다.
    arr = [[] for _ in range(V + 1)]

    ans = 0
    # E개의 노드 정보를 arr에 반영
    for _ in range(E):
        n1, n2 = map(int, input().split())
        arr[n1].append(n2)
        arr[n2].append(n1)
    # 출발 노드 S와 도착 노드 G
    S, G = map(int, input().split())

    # queue에 S을 추가, 리스트 visited[S]에 1 할당
    queue = deque()
    queue.append(S)
    visited = [0] * (V + 1)
    visited[S] = 1

    while queue:
        # queue의 첫 값
        tmp = queue.popleft()
        # queue의 첫 값의 연결된 노드들을 확인
        for i in arr[tmp]:
            # 방문한 적 없는 노드라면 queue와 visited에 값을 추가
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[tmp] + 1
        # G에 이미 방문했다면
        if visited[G] != 0:
            ans = visited[G] - 1
    # 테스트케이스 번호와 ans 출력
    print(f'#{case} {ans}')