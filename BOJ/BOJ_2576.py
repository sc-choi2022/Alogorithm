import sys
# 홀수를 저장하는 배열 numbers
numbers = []
for _ in range(7):
    number = int(sys.stdin.readline())
    if number%2:
        numbers.append(number)
# 배열 numbers을 정렬
numbers.sort()
# 홀수가 존재하는 경우
if numbers:
    print(sum(numbers))
    print(numbers[0])
# 홀수가 존재하지 않는 경우
else:
    print(-1)