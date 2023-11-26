from itertools import combinations
import sys

# 사람의 수 N
N = int(sys.stdin.readline())
# N번째 사람의 가장 큰 수를 저장하는 배열 scores
scores = [0] * (N+1)
# 이긴 사람 answer
answer = 0

for i in range(1, N+1):
    card = list(map(int, sys.stdin.readline().split()))
    coms = list(combinations(card, 3))
    # 카드로 만드는 수의 일의 자리수의 최댓값을 저장하는 변수 tmp
    tmp = 0
    for com in coms:
        tmp = max(tmp, sum(com)%10)
    # i번 선수의 최대 숫자
    scores[i] = tmp
    
# 이기는 가장 큰수 maxTmp
maxTmp = max(scores)
for j in range(1, N+1):
    if scores[j] == maxTmp:
        answer = j
# 게임에서 이긴 사람의 번호를 첫 번째 줄에 출력
# 이긴 사람이 두 명 이상일 경우에는 번호가 가장 큰 사람의 번호를 출력
print(answer)