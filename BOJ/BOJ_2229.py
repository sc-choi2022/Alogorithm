import sys

# 학생의 수 N
N = int(sys.stdin.readline())
# 점수를 저장하는 배열 scores
scores = list(map(int, sys.stdin.readline().split()))
# idx-1명으로 조를 짤 때 잘 짜여진 정도의 최댓값을 저장하는 배열 dp
dp = [0] * (N+1)

for i in range(N):
    dp[i+1] = dp[i]
    minS, maxS = scores[i], scores[i]
    j = i-1
    while j >= 0 and (scores[j] < minS or scores[j] > maxS):
        minS, maxS = min(minS, scores[j]), max(maxS, scores[j])
        dp[i+1] = max(dp[i+1], dp[j] + maxS-minS)
        j -= 1
# 조가 잘 짜여진 정도의 최댓값을 출력
print(dp[N])