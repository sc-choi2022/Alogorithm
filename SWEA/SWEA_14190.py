from collections import deque
import sys
sys.stdin = open('sampleinput.txt.txt')

T = int(input())
for case in range(1, T+1):
    # 세로 크기 N, 가로 크기 M
    N, M = map(int,input().split())
    # NxM 의 내용을 담은 리스트 arr
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 방문 위치를 확인
    visit = [[0]*N for _ in range(M)]
    # 꽃의 상태를 표시할 리스트 life
    life =[0 for _ in range(1250001)]
    # 씨앗을 심는 위치 i,j
    i, j = map(int,input().split())

    # deque를 활용하여 queue를 생성
    queue = deque()
    # 위치와 꽃이 피는 시작 날짜
    queue.append((i,j,1))
    # i,j에 방문위치 표시
    visit[i][j] = 1

    while queue:
        # 현재 위치, 현 위치에 꽃이 피는 날짜
        ci, cj, clife = queue.popleft()
        # 꽃이 피는 날짜를 life에 반영
        life[clife] += 1
        # 꽃이 지는 날짜를 life에 반영
        life[clife + arr[ci][cj]] -= 1
        # 상하좌우 방향에 대해 다음 위치를 ni,nj로 설정
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            ni = ci + di
            nj = cj + dj
            # ni,nj가 범위 안에 있고 방문한 적이 없는 곳이라면
            if 0<= ni < N and 0<= nj <M and visit[ni][nj] == 0:
                # 씨앗이 자랄 수 없는 토지라면 continue
                if arr[ni][nj] == 0:
                    continue
                # 아니라면
                else:
                    # ni,nj에 방문표시를 하고
                    visit[ni][nj] = 1
                    # 위치와 꽃이 필 다음 날을 queue에 추가
                    queue.append((ni,nj,clife+1))
    # 모든 날에 경과에 따른 꽃의 상태를 life에 반영
    # 현재 꽃의 수 now_cnt, 최대 꽃의 수 max_cnt, 최대 꽃인 날 maxDay을 0으로 초기화
    now_cnt = 0
    max_cnt = 0
    maxDay = 0
    # 모든 life 를 확인하며
    for day in range(1, 1250001):
        # 날이 지날때 마다 현재 꽃의 수를 확인
        now_cnt += life[day]
        # 현재 꽃의 수 now_cnt가 max_cnt보다 크다면 max_cnt에 now_cnt값을 저장, maxDay를 Day로 저장
        if now_cnt > max_cnt:
            max_cnt = now_cnt
            maxDay = day
    # 테스트 케이스 번호와 maxDay일 max_cnt개를 출력
    print(f'#{case} {maxDay}일 {max_cnt}개')