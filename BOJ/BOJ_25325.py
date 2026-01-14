from collections import defaultdict
import sys

# 학생 수 N
N = int(sys.stdin.readline())
# 학생의 이름을 저장하는 배열 names
names = list(sys.stdin.readline().rsplit())
# 좋아하는 학생수를 저장하는 딕셔너리 student
student = defaultdict(int)

for name in names:
    student[name] = 0

for _ in range(N):
    names = list(sys.stdin.readline().rsplit())
    for name in names:
        student[name] += 1

# 결과값을 정렬, 인기도 높은 순, 인기도가 같은 경우 이름 기준 오름차순
answer = list(sorted(student.items(), key=lambda x: (-x[1], x[0])))

# 학생 이름과 해당 학생을 좋아하는 학생 수를 공백으로 구분하여 출력
for a in answer:
    print(*a)