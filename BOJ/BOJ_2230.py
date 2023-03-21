import sys

# 수열 A를 이루는 정수의 개수 N, 차이의 기준 M
N, M = map(int, sys.stdin.readline().split())
# 수열 A
A = [int(sys.stdin.readline()) for _ in range(N)]
A.sort()
# 출력하는 가장 작은 차이 result
result = 2000000000

left, right = 0, 1
# left와 right가 수열A의 범위안에 있는 경우
while left < N and right < N:
    # 차이를 저장하는 변수 tmp
    tmp = A[right] - A[left]
    # 조건을 만족하는 경우 result 갱신, left 1 증가
    if tmp >= M:
        result = min(result, tmp)
        left += 1
    # 조건을 만족하지 않는 경우 right 1 증가
    elif tmp < M:
        right += 1
# result 출력
print(result)