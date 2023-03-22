import sys

# 수열의 길이 N, 부분합의 기준 S
N, S = map(int, sys.stdin.readline().split())
# 수열 sequence
sequence = list(map(int, sys.stdin.readline().split()))
# 두 포인트의 첫 기준 left, right, 부분합 tmpSum
left, right = 0, 0
tmpSum = 0
# 출력할 최소의 길이 result 100000 초기화
result = 100000

# 합을 만드는 것이 불가능한 경우
if sum(sequence) < S:
    print(0)
else:
    while True:
        # 합이 S 이상인 경우
        if tmpSum >= S:
            result = min(result, right - left)
            tmpSum -= sequence[left]
            left += 1
        # right이 sequence의 범위를 넘는 경우
        elif right == N:
            break
        else:
            tmpSum += sequence[right]
            right += 1
    # 구하고자 하는 최소의 길이를 출력
    print(result)