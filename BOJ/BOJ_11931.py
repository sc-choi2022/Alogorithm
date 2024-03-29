import sys

# 수의 개수 N
N = int(sys.stdin.readline())
# 수를 저장하는 배열 numbers
numbers = [int(sys.stdin.readline()) for _ in range(N)]
# numbers을 정렬
numbers.sort(reverse=True)

# N개의 줄에 내림차순으로 정렬한 결과를 한 줄에 하나씩 출력
for number in numbers:
    print(number)

# selection sort (시간초과)
N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

for i in range(N-1):
    for j in range(i+1, N):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
for number in numbers:
    print(number)