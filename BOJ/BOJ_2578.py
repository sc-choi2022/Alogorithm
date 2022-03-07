from pprint import pprint

bingo_board = [list(map(int, input().split())) for _ in range(5)]
calling = []

for c in range(5):
    calling.extend(list(map(int, input().split())))

while True:

    for c in range(len(calling)):
        cnt = 0
        for i in range(5):
            for j in range(5):
                if bingo_board[i][j] == calling[c]:
                    bingo_board[i][j] = 'x'
        pprint(bingo_board)
        print(c+1)

        for r in range(5):
            if bingo_board[r][:].count('x') == 5:
                cnt += 1

        for jj in range(5):
            col_cnt = 0
            for ii in range(5):
                if bingo_board[ii][jj] == 'x':
                    col_cnt += 1
            if col_cnt == 5:
                cnt += 1
        if cnt >= 3:
            print(c+1)
            break
    if cnt >= 3:
        break

