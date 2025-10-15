from itertools import permutations
import sys

while True:
    try:
        # 주어지는 테스트 케이스 S
        S = sys.stdin.readline().rstrip().split(' ')
        # 주어지는 집합 A, 위치 L
        A, L = S[0], int(S[1])

    except:
        break