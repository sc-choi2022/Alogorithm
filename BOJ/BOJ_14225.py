import sys

# 수열 S의 크기 N
N = int(sys.stdin.readline())
# 수열 S
S = sorted(list(map(int, sys.stdin.readline().split())))
# 수열 S의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수 answer
answer = 0

for s in S:
    # 현재까지의 합과 다음 수열의 숫자 사이에 값이 존재한다면
    if answer + 1 < s:
        break
    answer += s
# answer + 1 출력
print(answer + 1)