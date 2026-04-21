import sys

N, M = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))

top_score = -1
top_id = None

for _ in range(M):
    data = sys.stdin.readline().split()
    student_id, result = int(data[0]), data[1:]

