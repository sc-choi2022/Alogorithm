from collections import defaultdict
import sys

# 대회참가 학생 수 N
N = int(sys.stdin.readline())
# 학생의 소속 국가 번호, 학생 번호, 성적을 저장하는 배열 students
students = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 나라별 수상자 수를 저장하는 배열 country
country = defaultdict(int)
students.sort(key=lambda x:-x[2])

for i in range(N):
    # 학생의 소속국가 번호와 학생 번호, 점수 C, num, score
    C, num, score = students[i]
    if C in country and country[C] >= 2:
        continue
    # 소속국가 번호와 학생 번호를 하나의 빈칸을 사이에 두고 출력
    print(C, num)
    country[C] += 1
    # 메달 수상자가 결정된 경우 break
    if sum(country.values()) == 3:
        break