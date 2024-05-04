from itertools import permutations
import sys

# 순열을 이루는 자연수의 개수 N
N = int(sys.stdin.readline())
# 소문제 번호 number, 번호에 따른 나머지 K
number, *K = map(int, sys.stdin.readline().split())
K = tuple(K)

# 순열 permu
permu = list(permutations([x for x in range(1, N+1)], N))
permu.sort()

if number == 1:
    # k번째 수열을 나타내는 N개의 수를 출력
    print(*permu[K[0]-1])
elif number == 2:
    # 몇 번째 수열인지를 출력
    print(permu.index(K)+1)