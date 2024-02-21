import sys

# 학생의 수 N
N = int(sys.stdin.readline())
# 점수를 저장하는 배열 scores
scores = [float(sys.stdin.readline()) for _ in range(N)]
scores.sort()

# 하위 7명의 성적을 점수가 낮은 순으로 각 줄마다 출력
for score in scores[:7]:
    print('{:.3f}'.format(score))