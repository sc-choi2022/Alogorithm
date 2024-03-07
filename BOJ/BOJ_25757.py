import sys

# 플레이 신청 횟수 N, 플레이할 게임의 종류 game
N, game = map(str, sys.stdin.readline().rstrip().split())
# 플레이를 신청한 중복없는 사람을 저장하는 셋 people
people = set(sys.stdin.readline().rstrip() for _ in range(int(N)))
# people에 속한 인원 수 L
L = len(people)

# 임스가 플레이할 수 있는 최대 횟수를 출력
if game == 'Y':
    print(L)
elif game == 'F':
    print(L//2)
else:
    print(L//3)