import sys, copy
sys.stdin = open('input.txt')

for _ in range(1, 10+1):
    # 케이스 번호
    case = int(input())
    # 100 x 100 크기의 2차원 배열로 주어진 사다리
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 행의 방향 di, 열의 방향 dj에 대한 정보를 담은 리스트
    di = [0, 0 , -1]
    dj = [1, -1, 0]

    # 짧은 길이를 10000로 초기화
    # x의 위치를 담을 ans 0으로 초기화
    # 도착점의 모든 위치 담을 리스트 js 생성
    min_cnt = 10000
    ans = 0
    js = []

    # 99번 행의 1이 있는 위치를 찾아 리스트 js에 추가
    for t in range(100):
        if arr[99][t] == 1:
            js.append(t)

    # 도착지점의 j값 수만큼 진행하여 모든 가능성의 j위치에서 이동거리 확인
    for jj in range(len(js)):
        i = 99
        j = js[jj]
        cnt = 0
        # 리스트 arr를 deepcopy
        temp = copy.deepcopy(arr)
        # 행이 첫 줄에 도착할 때까지
        while i>0:
            # di, dj의 방향으로 움직인다.
            for d in range(3):
                ni = i + di[d]
                nj = j + dj[d]
                # di, dj에 의해 움직인 임시 위치 ni, nj가 범위를 벗어나지않고 지나갈 수 있는 1이라면
                if 0<= ni <= 99 and 0<= nj <= 99 and temp[ni][nj] == 1:
                    # i, j의 위치를 옮기고
                    i = ni
                    j = nj
                    # 지난 곳을 0으로 변경한다.
                    temp[i][j] = 0
                    cnt += 1
        # 이동거리를 min_cnt와 비교하여 필요하다면 재설정
        if min_cnt > cnt:
            min_cnt = cnt
            # 그 위치의 x좌표를 ans에 할당
            ans = j

    # 테스트 케이스의 번호와 출발점의 x좌표 출력
    print(f'#{case} {ans}')