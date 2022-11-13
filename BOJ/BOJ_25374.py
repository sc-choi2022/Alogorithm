import sys
# 학생의 수 N
N = int(sys.stdin.readline())
# N개의 점수를 담을 리스트 scores
scores = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
# 등급 기준을 담은 리스트 grades
grades = [0.04, 0.11, 0.23, 0.4, 0.6, 0.77, 0.89, 0.96]
# 출력할 인원수를 담을 리스트 result
result = [0] * 9
# 기준이 되는 점수를 변수 previous에 저장하고 초기값을 scores[0]으로 지정
previous = scores[0]
# rank 0으로 초기화
rank = 0

for idx, score in enumerate(scores):
    # 경계값이라면 result[rank] 1 증가
    if score == previous:
        result[rank] += 1
    else:
        rate = (idx + 1) / N
        if rate <= grades[0]:
            result[0] += 1
            rank = 0
        elif rate <= grades[1]:
            result[1] += 1
            rank = 1
        elif rate <= grades[2]:
            result[2] += 1
            rank = 2
        elif rate <= grades[3]:
            result[3] += 1
            rank = 3
        elif rate <= grades[4]:
            result[4] += 1
            rank = 4
        elif rate <= grades[5]:
            result[5] += 1
            rank = 5
        elif rate <= grades[6]:
            result[6] += 1
            rank = 6
        elif rate <= grades[7]:
            result[7] += 1
            rank = 7
        else:
            result[8] += 1
            rank = 8
    # previous 값을 갱신
    previous = score
# result값 출력
print(*result, sep='\n')