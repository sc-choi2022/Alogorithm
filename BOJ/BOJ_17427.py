import sys

# 자연수 N
N = int(sys.stdin.readline())
# g(N)
answer = 0

for i in range(1, N+1):
    # N이하의 자연수 중에서 i를 약수로 갖는 개수는 N/i
    answer += (N//i)*i
# g(N)를 출력
print(answer)