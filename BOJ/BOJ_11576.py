import sys

# 진법 A, 진법 B
A, B = map(int, sys.stdin.readline().split())
# A진법으로 나타낸 숫자의 자리수의 개수 M
M = int(sys.stdin.readline())
# A진법을 이루고 숫자를 저장하는 배열 numbers
numbers = reversed(list(map(int, sys.stdin.readline().split())))
# A진법을 10진법으로 변경한 수 ten, A진법의 자리수 idx
ten, idx = 0, 0

for number in numbers:
    ten += number*A**idx
    idx += 1

# B진법을 저장하는 배열 numberInB
numberInB = []

# 10진법 수를 B진법으로 변환
while ten:
    numberInB.append(ten%B)
    ten //= B
# A진법으로 나타낸 수를 B진법으로 변환하여 출력
print(*reversed(numberInB))