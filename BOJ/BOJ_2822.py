import sys
# 참가자의 번호와 점수를 저장하는 배열 scores
scores = [(0, 0) for _ in range(8)]

for i in range(1, 8+1):
    scores[i-1] = (i, int(sys.stdin.readline()))
# 가장 높은 점수 5개를 위해 scores 정렬
scores.sort(key=lambda x:-x[1])

# 참가자의 총점과 상위 5개의 점수를 가진 참가자의 번호를 저장하는 배열 answer
total = 0
answer = [0]*5
for j in range(5):
    total += scores[j][1]
    answer[j] = scores[j][0]
# 참가자의 총점을 출력
print(total)
# 어떤 문제가 최종 점수에 포함되는지를 공백으로 구분하여 출력
print(*sorted(answer))