T = int(input())
for case in range(1, T+1):
    # 최대 노드의 개수 V, 간선의 개수 E
    V, E = map(int, input().split())
    # 출발 도착 노드로 간선 정보 E개를 리스트 arrs에 담는다.
    arrs = [list(map(int, input().split())) for _ in range(E)]
    # 출발 노드 S, 도착노드 G
    S, G = map(int,input().split())
    # 노드번호와 인덱스를 맞추기 위해 노드 수+1 개의 grid를 만든다.
    grid = [[0]*(V+1) for _ in range(V+1)]
    # arrs의 arr의 정보로 간선의 정보를 grid에 반영
    for arr in arrs:
        grid[arr[0]][arr[1]] = 1

    # 스택과 방문정보를 담을 리스트 stack, visited를 초기화
    stack = []
    visited = []

    # 출발 노드 S를 stack과 visited 리스트에 추가
    stack.append(S)
    visited.append(S)
    # 경로에 대한 정답 ans 값 초기화
    ans = 0

    # stack이 empty가 될 때까지 진행
    while stack:
        # stack의 top에 있는 값을 temp로 할당
        temp = stack[-1]

        # 모든 노드를 확인하는 for문
        for node in range(1, V+1):
            # 간선이 연결, 방문한 적이 없다면 stack과 visited에 추가
            if grid[temp][node] == 1 and node not in visited:
                stack.append(node)
                visited.append(node)
                break
        else:
            # 아닐 경우 stack의 top값 제거
            stack.pop()
        # 노드가 도착 지점을 방문하여 visited에 값이 있다면
        if G in visited:
            # ans 값을 1로 할당
            ans = 1
            break
    # 테스트 케이스 번호와 답 출력
    print(f'#{case} {ans}')