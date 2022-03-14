import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for case in range(1, T + 1):
    # 최대 노드의 수 V, 간선의 수 E
    V, E = map(int, input().split())
    # E의 간선에 대한 정보를 담을 리스트 grid
    grid = [[0] * 51 for _ in range(51)]
    # 노드의 정보를 담을 리스트 node
    node = []

    # grid를 정보에 맞게 채우고 모든 노드의 정보를 리스트 node에 추가하는 for문
    for _ in range(E):
        start, end = map(int, input().split())
        grid[start][end] = 1
        node.append(start)
        node.append(end)
    # 출발 노드 S, 도착노드 G
    S, G = map(int, input().split())
    # 리스트 node 정렬
    node.sort()

    # 시작점을 stack과 visited에 추가
    stack = [S]
    visited = [S]

    # 답 ans 값 초기화
    ans = 0
    # stack이 비어있게 될 때까지
    while stack:
        # temp는 stack의 top값
        temp = stack[-1]

        # 정보에 있던 모든 노드에 대해
        for n in range(node[0], node[-1] + 1):
            # 간선이 있고 방문한 적이 없는 노드라면 stack과 visited에 추가
            if grid[temp][n] == 1 and n not in visited:
                stack.append(n)
                visited.append(n)
                break
        # for문에서 break를 만나지 못하였다면
        else:
            # stack의 top값 제거
            stack.pop()

        # 목적지에 도달했다면 ans에 1을 할당
        if G in visited:
            ans = 1
            break
    # 테스트 케이스 번호와 ans 출력
    print(f'#{case} {ans}')