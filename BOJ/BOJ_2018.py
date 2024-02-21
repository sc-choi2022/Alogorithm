import sys

# 자연수 N
N = int(sys.stdin.readline())

# 연속한 수의 범위 left, right
left, right = 1, 1
# 범위 내의 합 number
number = 1

# 자연수 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수 answer
answer = 1

while right < N:
    if number == N:
        answer += 1
        right += 1
        number += right
    elif number > N:
        number -= left
        left += 1
    else:
        right += 1
        number += right

# 자연수 N을 몇 개의 연속된 자연수의 합으로 나타내는 가지수를 출력
print(answer)