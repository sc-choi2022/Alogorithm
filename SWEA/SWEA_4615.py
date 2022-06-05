# 테스트 케이스 수 T
T = int(input())

for case in range(1, T + 1):
    # 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M
    N, M = map(int, input().split())

    # N에 따라 보드의 크기가 정해진다.
    board = [[0] * N for _ in range(N)]

    # board의 흑돌과 백돌의 기본 위치를 반영한다.
    # 1이면 흑돌, 2이면 백돌
    board[N//2 - 1][N//2 - 1] = 2
    board[N//2 - 1][N//2] = 1
    board[N//2][N//2 - 1] = 1
    board[N//2][N//2] = 2

    for i in range(M):
        # 돌의 위치와 색상
        ii, jj, colour = map(int, input().split())
        ii, jj = ii - 1, jj - 1
        flip = []

        for di, dj in (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1):
            ni, nj = ii + di, jj + dj
            while True:
                if ni < 0 or ni > N-1 or nj < 0 or nj > N - 1 or board[ni][nj] == 0:
                    # 다른 색을 만나고 다시 같은 색을 만나지 못했거나 빈 자리를 만난경우 flip을 초기화
                    flip = []
                    break
                if board[ni][nj] == colour:
                    # 다른 색을 만나고 다시 자신의 색을 만난 경우
                    break
                else:
                    flip.append((ni, nj))
                ni, nj = ni + di, nj + dj

            # 뒤집어야하는 flip안의 모든 위치 값들을 colour로 변경해준다.
            for fi, fj in flip:
                board[fi][fj] = colour

        board[ii][jj] = colour

    # 출력해줄 흑돌과 백돌의 변수 black과 white를 선언
    black = 0
    white = 0

    # 돌의 수를 count한다.
    for b in board:
        black += b.count(1)
        white += b.count(2)

    # 조건에 맞게 출력
    print(f'#{case} {black} {white}')