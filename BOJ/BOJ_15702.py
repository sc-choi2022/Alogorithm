import sys

# 문제의 개수 N, 응시자의 수 M
N, M = map(int, sys.stdin.readline().split())
# 문제의 배점을 저장하는 배열 scores
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

# 가장 높은 점수를 얻은 학생의 번호와 점수를 공백으로 구분해 출력
# 가장 높은 점수를 얻은 학생이 여러 명이라면, 수험 번호가 가장 작은 것을 출력
print(top_id, top_score)