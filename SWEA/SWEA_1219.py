import sys
sys.stdin = open('input.txt')

# 10번의 테스트 케이스를 진행하기 위한 for문
for _ in range(10):
    # 테스크 케이스 번호와 길의 총 개수를 각각 case와 N에 할당
    case, N = map(int, input().split())
    # 순서쌍에 대한 정보를 arr에 모두 할당
    arr = list(map(int, input().split()))
    # 순서쌍의 정보를 확인하여 입력할 리스트 grid 생성
    grid = [[0]*100 for _ in range(100)]

    # arr에 담긴 값을 각 정점과 도착하는 정점의 번호로 구분하여 순서쌍 위치에 1을 할당
    for i in range(0, N*2, 2):
        grid[arr[i]][arr[i+1]] = 1

    # 스택을 담을 리스트 stack과 방문정보를 저장할 visted 리스트 초기화
    stack = []
    visited = []

    # 출발점이 0으로 지정되어 있기 때문에 stack과 visted에 0을 추가
    stack.append(0)
    visited.append(0)

    # 답으로 출력할 ans를 초기화
    ans = 0
    # stack이 empty가 될 때까지
    while stack:
        # stack에 top에 있는 값을 temp에 할당
        temp = stack[-1]

        # 0~99까지의 노드에서
        for node in range(100):
            # grid의 값이 1이며 방문정보가 없는 노드를 stack과 vistied에 추가
            if grid[temp][node] == 1 and node not in visited:
                stack.append(node)
                visited.append(node)
                break
        # for문의 반복이 끝날 때까지 break되지 않았다면 top 노드에서 갈수 있는 모든 node를 간 것이므로
        # stack의 top값을 pop
        else:
            stack.pop()

        # 도착 지점인 99에 방문한 기록이 있다면
        if 99 in visited:
            # ans에 1을 할당하고 while문을 탈출
            ans = 1
            break
    # 테스트 케이스 번호와 답을 출력
    print(f'#{case} {ans}')