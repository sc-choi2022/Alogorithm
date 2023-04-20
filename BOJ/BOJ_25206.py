import sys

grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0,
         'D+':1.5, 'D0':1.0, 'F':0}

# 전공과목별 합 score, total
score, total = 0, 0

for _ in range(20):
    # 수강한 전공과목의 과목명, 학점, 등급
    a, b, c = sys.stdin.readline().rstrip().split()
    # b를 float로 변경
    b = float(b)
    if c != 'P':
        total += b
        score += b * grade[c]

# 전공평점을 출력
print('%.6f' % (score / total))