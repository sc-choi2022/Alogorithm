from collections import deque
import sys

# 주어지는 배열 numbers를 최대합이 되도록 계산하는 함수 add
def add(numbers):
    # 배열을 deque로 변경
    numbers = deque(numbers)
    # 반환할 값을 저장하는 변수 added
    added = 0
    while len(numbers) > 1:
        added += numbers.popleft() * numbers.popleft()
    # while문으로 계산된 added에 numbers의 남은 값을 더하여 return
    return added + sum(numbers)

# 수열의 크기 N
N = int(sys.stdin.readline())
# 수열을 담을 배열 pos, neg 각각 양수, 음수
pos, neg = [], []
# 출력할 최대합 maxSum
maxSum = 0

# 모든 값을 양수와 음수로 구분하여 pos, neg에 저장
for _ in range(N):
    number = int(sys.stdin.readline())
    if number > 1:
        pos.append(number)
    elif number == 1:
        maxSum += 1
    else:
        neg.append(number)
# pos와 neg을 정렬
pos.sort(reverse=True)
neg.sort()

# maxSum에 add(pos)와 add(neg)의 반환값을 반영
maxSum += add(pos) + add(neg)
# maxSum을 출력
print(maxSum)