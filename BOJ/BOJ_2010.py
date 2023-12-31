import sys

N = int(sys.stdin.readline())
# 최대로 전원에 연결될 수 있는 컴퓨터의 수
answer = 0

for _ in range(N):
    answer += int(sys.stdin.readline())
# 멀티탭에 연결하는 과정에서 사용되는 플러그수 N-1를 뺀 값을 출력
print(answer - (N-1))