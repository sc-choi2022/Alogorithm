import sys

# 전체 기간 일수 N, 기간 일수 X
N, X = map(int, sys.stdin.readline().split())
# 명수를 저장하는 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))

# X일 동안 가장 많이 들어온 망문자 수 answer, 최대인원인 기간의 수 cnt
answer, cnt = sum(numbers[:X]), 1

# 범위의 값을 저장하는 변수 tmp
tmp = sum(numbers[:X])
for i in range(X, N):
    tmp -= numbers[i-X]
    tmp += numbers[i]
    # 최대 방문자 수 인 경우 answer와 cnt 값 초기화
    if tmp > answer:
        answer = tmp
        cnt = 1
    # 최대 방문자 수와 동일한 경우 cnt 1 증가
    elif tmp == answer:
        cnt += 1

# X일 동안 가장 많이 들어온 방문자 수와 기간 내 개수 출력
if answer:
    print(answer)
    print(cnt)
# 최대 방문자 수 0인 경우 SAD 출력
else:
    print('SAD')