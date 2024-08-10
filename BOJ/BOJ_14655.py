import sys

# 동전의 수 N
N = int(sys.stdin.readline())
# 첫번째와 두번째 라운드의 동전의 배열 R1
R1 = list(map(abs, map(int, sys.stdin.readline().split())))
R2 = list(map(abs, map(int, sys.stdin.readline().split())))
# 이번 게임에서 획득할 점수를 출력
print(sum(R1) + sum(R2))