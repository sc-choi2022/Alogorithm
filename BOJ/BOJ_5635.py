import sys

# 학생의 수 N
N = int(sys.stdin.readline())
# 학생의 정보를 담을 리스트 student
student = [0] * N

# N개의 정보를 student에 저장
for i in range(N):
    name, day, month, year = sys.stdin.readline().split()
    student[i] = [int(year), int(month), int(day), name]

# year, month, day를 기준으로 정렬
student.sort()
# 가장 나이가 적은 사람의 이름 출력
print(student[-1][3])
# 가장 나이가 많은 사람 이름을 출력
print(student[0][3])