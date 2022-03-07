# 빙고판 5x5 bingo_board
bingo_board = [list(map(int, input().split())) for _ in range(5)]
# 사회자가 부르는 수를 담을 리스트
calling = []
# 사회자가 부르는 수를 1x25 배열로 담는다.
for c in range(5):
    calling.extend(list(map(int, input().split())))

while True:
    # 사회자의 부르는 수에 따라 for문 진행
    for c in range(len(calling)):
        # 빙고의 수 cnt 초기화
        cnt = 0
        # 부르는 수에 따라 빙고에 표시
        for i in range(5):
            for j in range(5):
                if bingo_board[i][j] == calling[c]:
                    bingo_board[i][j] = 'x'
        
        # 가로에 빙고수 확인
        for r in range(5):
            if bingo_board[r][:].count('x') == 5:
                cnt += 1
        
        # 세로 빙고수 확인
        for jj in range(5):
            col_cnt = 0
            for ii in range(5):
                if bingo_board[ii][jj] == 'x':
                    col_cnt += 1
            if col_cnt == 5:
                cnt += 1
        
        # 대각선의 빙고수를 확인
        a_cnt = 0
        b_cnt = 0
        for a in range(5):
            if bingo_board[a][a] == 'x':
                a_cnt += 1
            if bingo_board[a][-a-1] == 'x':
                b_cnt += 1
        if a_cnt == 5:
            cnt += 1
        if b_cnt == 5:
            cnt += 1

        # 빙고수가 3개 이상이라면 출력 후 while문 탈출
        if cnt >= 3:
            print(c+1)
            break
    if cnt >= 3:
        break

