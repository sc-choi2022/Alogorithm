import sys

N, M = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))

top_score = -1
top_id = None

for _ in range(M):
    student_id, result = map(int, sys.stdin.readline().split())