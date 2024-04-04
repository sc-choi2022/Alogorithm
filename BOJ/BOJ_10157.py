import sys

# 좌석의 위치를 찾는 함수 find
def find(number):
    if number > R*C:
        print(0)
        return
    # 좌석의 번호를 확인하는 배열 seat
    seat = [[0]*C for _ in range(R)]
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    # 초기 위치 (si, sj) 초기위치의 초기값 1, 방향의 초기값 0
    si, sj = R-1, 0
    seat[si][sj] = 1
    d = 0

    while True:
        if seat[si][sj] == number:
            print(sj+1, R-si)
            return

        di, dj = direction[d]
        ni, nj = si + di, sj + dj
        if 0 <= ni < R and 0 <= nj < C and not seat[ni][nj]:
            seat[ni][nj] = seat[si][sj] + 1
            si, sj = ni, nj
        else:
            d = (d+1)%4

# 공연장의 크기 C, R
C, R = map(int, sys.stdin.readline().split())
# 찾아야하는 번호 K
K = int(sys.stdin.readline())
# 대기 순서 K의 좌석 혹은 불가능하다면 0 출력
find(K)