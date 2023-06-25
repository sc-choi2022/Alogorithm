from collections import deque
import sys

# 빨대의 개수 N
N = int(sys.stdin.readline())
# N개의 숫자를 저장하는 배열 numbers
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()
# 삼각형 세 변의 길이의 합의 최댓값 answer
answer = -1
able = deque(numbers[-2+N:])

for i in range(N-3, -1, -1):
    able.appendleft(numbers[i])
    if able[2] < able[0] + able[1]:
        answer = sum(able)
        break
    able.pop()
# 삼각형 세 변의 길이의 합의 최댓값을 출력
# 만약 삼각형을 만들 수 없으면 -1을 출력
print(answer)

# 방법 2
import sys

# 빨대의 개수 N
N = int(sys.stdin.readline())
# N개의 숫자를 저장하는 배열 numbers
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort(reverse=True)
# 삼각형 세 변의 길이의 합의 최댓값 answer
answer = -1

for idx in range(N-2):
    if numbers[idx] < numbers[idx+1] + numbers[idx+2]:
        answer = numbers[idx] + numbers[idx+1] + numbers[idx+2]
        break
# 삼각형 세 변의 길이의 합의 최댓값을 출력
# 만약 삼각형을 만들 수 없으면 -1을 출력
print(answer)