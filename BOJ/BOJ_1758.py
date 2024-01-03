import sys

# 앞에 서 있는 사람의 수 N
N = int(sys.stdin.readline())
# 주어지는 팁을 저장하는 배열 tips
tips = [int(sys.stdin.readline()) for _ in range(N)]
tips.sort(reverse=True)
# 팁의 최댓값 answer
answer = 0
for i in range(N):
    answer += (tips[i] - i) if (tips[i] - i) > 0 else 0
# 팁의 최댓값을 출력
print(answer)