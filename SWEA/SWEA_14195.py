from copy import deepcopy
import sys
sys.stdin = open('sampleinput.txt')

# bfs를 통해 value로 주어진 미생물의 개체수와 개체의 크기를 구한다.
def bfs(si, sj, value):
    # 각 미생물의 개체수와 개체의 크기를 비교해 큰 값을 저장할 max_cnt global 처리
    global A_cnt, B_cnt, max_cnt
    # 빈 리스트 queue를 생성
    queue = []
    # queue에 (si,sj) 추가
    queue.append((si, sj))
    # 추가한 후에 값을 변경
    tst[si][sj] = '_'
    # cnt 1 증가
    cnt = 1
    # 현재 개체의 크기를 모두 파악할 때까지 queue진행
    while queue:
        # ci,cj 변수에 queue(0) 할당
        ci, cj = queue.pop(0)
        # 상하좌우 방향에 대한 다음 위치 ni,nj 정하여
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni = ci + di
            nj = cj + dj
            # 범위안에 있고 개체와 동일한 종류 일때
            if 0<= ni < N and 0<= nj < M and tst[ni][nj] == value:
                # 값을 바꿔주고 queue에 위치 추가 후 cnt 1증가
                tst[ni][nj] = '_'
                queue.append((ni, nj))
                cnt += 1
    # 개체 크기가 파악되면 value에 맞는 cnt변수에 값을 1증가
    # 현재 개체의 크기와 max_cnt를 비교하여 큰 값을 max_cnt에 할당
    if value == 'A':
        A_cnt += 1
        max_cnt = max(max_cnt, cnt)
    else:
        B_cnt += 1
        max_cnt = max(max_cnt, cnt)

# 테스트 케이스 수
T = int(input())
for case in range(1, T+1):
    N, M = map(int, input().split())
    # 미생물 위치의 원본을 리스트 og에 할당
    og = [list(input()) for _ in range(N)]
    # 값을 확인하고 변경해줄 og와 동일한 리스트 tst 생성
    tst = deepcopy(og)
    # A, B 개체의 수 A_cnt, B_cnt, 개체의 크기 max_cnt 값을 0으로 초기화
    A_cnt = 0
    B_cnt = 0
    max_cnt = 0
    # 미생물이 있는 위치를 확인하여
    for i in range(N):
        for j in range(M):
            if tst[i][j] != '_':
                # 미생물의 위치와 미생물의 종류를 parameter로 하여 bfs 실행
                bfs(i, j, tst[i][j])
    # 테스트케이스와 A, B의 개체수, 최대 개체 크기를 출력
    print(f'#{case} {A_cnt} {B_cnt} {max_cnt}')