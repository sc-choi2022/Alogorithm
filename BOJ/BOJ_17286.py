import sys

cat = tuple(map(int, sys.stdin.readline().split()))
people = list(list(map(int, sys.stdin.readline().split())) for _ in range(3))