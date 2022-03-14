import sys
sys.stdin = open('input.txt')

# 10개의 테스트 케이스
for _ in range(10):
    # 테스크케이스 번호 case 길의 총 개수 N
    case, N = map(int, input().split())
    # 순서쌍을 담을 리스트 arr
    arr = list(map(int, input().split()))
    # 순서쌍의 정보를 통해 방향을 반영한 정보를 담을 리스트 grid
    grid = [[0]*100 for g in range(100)]

    # 리스트 arr의 정보를 grid에 반영하는 for문
    for i in range(0, 2*N, 2):
        grid[arr[i]][arr[i+1]] = 1

    # stack과 visited 리스트 초기화
    stack = []
    visited = []

    # 시작위치 0을 stack과 visited의 첫 값으로 추가
    stack.append(0)
    visited.append(0)

    # 답을 0으로 초기화
    ans = 0
    # stack이 비어있을 때까지 while문 진행
    while stack:
        # stack의 top을 변수 temp에 할당
        temp = stack[-1]

        # 모든 node에 대해
        for node in range(100):
            # temp에서 node로 가는 길이 있고, visited에 없는 방문한 적 없는 node일 경우
            if grid[temp][node] == 1 and node not in visited:
                # stack과 visited에 추가
                stack.append(node)
                visited.append(node)
                # node로 넘어간다.
                break
        # for문에서 break를 만나지 않았다면 temp에서 node로 가는 길이 없는 것
        else:
            # stack의 top값을 pop
            stack.pop()

        # visited에 99가 있다. 마지막 node에 도착했다면
        if 99 in visited:
            # ans에 1을 할당
            ans = 1
            #while문을 벗어난다.
            break
    # 테스트 케이스 번호와 답을 출력
    print(f'#{case} {ans}')