from itertools import permutations
import sys

# 질문횟수 N
N = int(sys.stdin.readline())
data = [str(i) for i in range(1, 9+1)]
number = list(permutations(data, 3))