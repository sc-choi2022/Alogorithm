from collections import defaultdict
import sys

N = int(sys.stdin.readline())
names = list(sys.stdin.readline().rsplit())
student = defaultdict(int)
for name in names:
    student[name] = 0

for _ in range(N):
    names = list(sys.stdin.readline().rsplit())
    for name in names:
        student[name] += 1

answer = list(sorted(student.items(), key=lambda x: (-x[1], x[0])))

for a in answer:
    print(*a)