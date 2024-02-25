import sys

# 승환이 앞에 서 있는 학생들의 수 N
N = int(sys.stdin.readline())
# 승환이 앞에 서있는 모든 학생들의 번호를 저장하는 배열 numbers
numbers = list(map(int, sys.stdin.readline().split()))
# 대기열 stack
stack = []
# 간식을 배부받는 번호 snack
snack = 1

for number in numbers:
    # 간식을 배부 받는 경우
    if number == snack:
        snack += 1
    # 대기열에 가는 경우
    else:
        # 순서에 맞춰 대기열이 가능한 경우
        if (not stack) or (stack and stack[-1] > number):
            stack.append(number)
        # 간식배부가 불가능한 경우
        else:
            break
    while stack:
        if stack[-1] != snack:
            break
        snack += 1
        stack.pop()

# 간식을 받을 수 있으면 Nice, 그렇지 않다면 Sad 출력
print('Sad' if stack else 'Nice')