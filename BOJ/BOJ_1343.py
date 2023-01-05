import sys

# 보드판의 X와 .의 정보를 저장하는 변수 board
board = sys.stdin.readline().strip()
# 덮을 수 있는 폴리노미오를 replace
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

# 덮을 수 없는 경우 -1 출력
if 'X' in board:
    print(-1)
# 모두 덮었다면 board 출력
else:
    print(board)