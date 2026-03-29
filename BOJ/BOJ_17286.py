from itertools import permutation
import sys

cat = tuple(map(int, sys.stdin.readline().split()))
people = list(list(map(int, sys.stdin.readline().split())) for _ in range(3))

M_move = 1e9
for P in permutation([1, 2, 3], 3):
    x, y = people[0][0], people[0][1]

    move = 0
    for p in P:
        move += (abs(x - people[i][0])**2 + abs(y - people[i][1])**2)**0.5