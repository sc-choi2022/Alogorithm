import sys

N, M = map(int, sys.stdin.readline().split())
scores = list(map(int, sys.stdin.readline().split()))

top_score = -1
top_id = None

for _ in range(M):
    data = sys.stdin.readline().split()
    student_id, result = int(data[0]), data[1:]

    total = 0
    for i in range(N):
        if result[i] == 'O':
            total += scores[i]
    if total > top_score or (total == top_score and student_id < top_id):
        top_score = total
        top_id = student_id

print(top_id, top_score)