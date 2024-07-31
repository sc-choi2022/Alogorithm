import sys

# 집의 위치 N
N = int(sys.stdin.readline())
# 보도블럭에 쓰여있는 글자 words
words = sys.stdin.readline().rstrip()
# 보도블록에 도달했을 때의 최솟값을 저장하는 배열 dp
# 기본 값을 최댓값 1e6, 0번 위치의 값을 0으로 초기화
dp = [1e6] * N
dp[0] = 0

for i in range(N):
    for j in range(i+1, N):
        if dp[i] != 1e6:
            if words[i] == 'B' and words[j] == 'O':
                dp[j] = min(dp[j], dp[i] + (j-i)**2)
            elif words[i] == 'O' and words[j] == 'J':
                dp[j] = min(dp[j], dp[i] + (j-i)**2)
            elif words[i] == 'J' and words[j] == 'B':
                dp[j] = min(dp[j], dp[i] + (j-i)**2)

# 스타트가 링크를 만나는데 필요한 에너지 양의 최솟값을 출력
# 스타트가 링크를 만날 수 없는 경우에는 -1을 출력
print(dp[-1] if dp[-1] != 1e6 else -1)