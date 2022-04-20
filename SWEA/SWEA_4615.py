import sys
sys.stdin = open('sample_input.txt')
from pprint import pprint

T = int(input())
for case in range(1, T+1):
    # 한변의 길이 N, 놓을 돌의 개수
    N, M = map(int, input().split())
    # idx를 맞추기 위해 (N + 1) x (N + 1) 크기의 배열 생성
    board = [[0]*(N+1) for _ in range(N+1)]

    # 초기 돌의 4곳을 표시
    board[N//2][N//2] = 2
    board[N//2][N//2+1] = 1
    board[N//2+1][N//2] = 1
    board[N//2+1][N//2+1] = 2

    # M개의 줄의 정보를 활용하여 돌을 놓기
    for _ in range(M):
        # 좌표 ni, nj, 돌의 종류 color
        si, sj, color = map(int, input().split())
        board[si][sj] = color
        # 규칙에 따라 돌의 색이 바꾼다.
        for di, dj in ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)):
            # 돌의 색이 바뀔 가능성이 있는 위치값들을 담을 리스트 s
            s = []
            # k만큼 범위내에서 움직인다.
            for k in range(1, N):
                ni = si + di*k
                nj = sj + dj*k
                # ni, nj가 범위 내에 존재
                if 1<= ni <= N  and 1<= nj <= N:
                    # board[ni][nj] == 0이면 중지
                    if board[ni][nj] == 0:
                        break
                    # board[ni][nj]이 현재 값과 동일하면 s의 모든 위치의 값을 color로 변경
                    elif board[ni][nj] == color:
                        for ci, cj in s:
                            board[ci][cj] = color
                    # board[ni][nj]이 다른 색이면 s에 위치 추가
                    else:
                        s.append((ni, nj))
                # 범위를 벗어나면 break
                else:
                    break
    # 흑돌과 흰돌의 수 bcnt, wcnt
    bcnt = wcnt = 0
    for b in board:
        bcnt += b.count(1)
        wcnt += b.count(2)
    # 테스트케이스 번호와 흑돌의 수, 흰돌의 수 출력
    print(f'#{case} {bcnt} {wcnt}')