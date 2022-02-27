import sys
sys.stdin = open('input.txt')
for _ in range(1, 10+1):
    # 케이스 번호
    case = int(input())
    # 100 x 100 크기의 2차원 배열로 주어진 사다리
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 행의 방향 di, 열의 방향 dj에 대한 정보를 담은 리스트
    di = [0, 0 , -1]
    dj = [1, -1, 0]

    # 2가 있는 위치부터 올라가는 방법
    # 행의 시작을 99로 시작
    i = 99
    j = 0
    # 99번 행의 2가 있는 위치를 찾아 열 j의 초기값으로 설정
    for t in range(100):
        if arr[99][t] == 2:
            j = t

    # 행이 첫 줄에 도착할 때까지
    while i>0:
        # di, dj의 방향으로 움직인다.
        for d in range(3):
            ni = i + di[d]
            nj = j + dj[d]
            # di, dj에 의해 움직인 임시 위치 ni, nj가 범위를 벗어나지않고 지나갈 수 있는 1이라면
            if 0<= ni <= 99 and 0<= nj <= 99 and arr[ni][nj] == 1:
                # i, j의 위치를 옮기고
                i = ni
                j = nj
                # 지난 곳을 0으로 변경한다.
                arr[i][j] = 0
    # 테스트 케이스의 번호와 출발점의 x좌표 출력
    print(f'#{case} {j}')