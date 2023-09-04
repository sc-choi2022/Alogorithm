import sys

# M이상 N이하의 기준
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
# 가장 작은 완전제곱수
minimum = 0
# 완전제곱수의 합
answer = 0
for i in range(int(M**.5), int(N**.5)+1):
    if M <= i**2 <= N:
        if not minimum:
            minimum = i**2
        answer += i**2
# 완전제곱수가 있다면 출력 없다면 -1 출력
print(answer if answer else -1)
# 완전제곱수가 있는 경우 minimum 출력
if answer:
    print(minimum)