import sys

scores = [0] * 5
for i in range(5):
    scores[i] = sum(map(int, sys.stdin.readline().split()))
# 우승자의 번호와 그가 얻은 점수를 출력
print(scores.index(max(scores))+1, max(scores))