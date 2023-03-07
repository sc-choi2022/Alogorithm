import sys

# 좌석의 수 N
N = int(sys.stdin.readline())

# 좌석 seat
seat = list(sys.stdin.readline())
# 컵홀더의 개수 holder
holder = len(seat) - seat.count('L')//2

# 컵을 컵홀더에 놓을 수 있는 최대 사람의 수를 출력
print(N if holder > N else holder)

#

# 좌석의 수 N
N = int(sys.stdin.readline())
# 좌석 seat
seat = sys.stdin.readline().rstrip()
if 'LL' in seat:
    seat = seat.replace('LL', 'S')
    print(len(seat) + 1)
else:
    print(N)