from itertools import permutation
import sys

cat = tuple(map(int, sys.stdin.readline().split()))
people = list(list(map(int, sys.stdin.readline().split())) for _ in range(3))

M_move = 1e9
for p in permutation([1, 2, 3], 3):
    x, y = people[0][0], people[0][1]

    move = 0