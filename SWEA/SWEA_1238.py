from collections import deque
import sys
sys.stdin = open('input.txt')

for case in range(1, 10 + 1):
    # 데이터의 길이 N, 시작 점 S
    N, S = map(int, input().split())
    # N개의 데이터를 받은 리스트 info
    info = list(map(int, input().split()))
    # info에 값 중 가장 큰 값 M
    M = max(info)

    # info의 값을 정리해 저장할 M + 1의 크기의 리스트 arr
    arr = [[] for _ in range(M + 1)]

    # info에 값을 arr에 저장
    for i in range(0, N, 2):
        arr[info[i]].append(info[i + 1])

    # 연락을 할 때 bfs를 활용할 queue
    # 연락할 모든 번호를 담을 리스트 visited와 그 인덱스와 순서를 담을 리스트visited_idx
    queue = deque()
    queue.append(S)
    visited = []
    visited.append(S)
    visited_idx = [0] * (M + 1)
    visited_idx[S] = 1
    # visited_idx를 기준으로 마지막 연락한 사람들을 담을 리스트 ans
    ans = []
    # bfs를 진행
    while queue:
        tmp = queue.popleft()
        for t in arr[tmp]:
            # t가 visited에 없다면
            if t not in visited:
                queue.append(t)
                visited.append(t)
                # visited_idx는 이전 값에 1을 다한 값을 visited_idx[t]에 할당
                visited_idx[t] += visited_idx[tmp] + 1
    # 모든 연락이 끝난 후
    # 가장 마지막 연락한 값을 찾고
    MM = max(visited_idx)
    # 그 값을 value로 갖는 idx들을 ans에 추가
    for idx, value in enumerate(visited_idx):
        if value == MM:
            ans.append(idx)
    # 테스트 케이스 번호와 ans의 값 중 가장 큰 값을 출력
    print(f'#{case} {max(ans)}')