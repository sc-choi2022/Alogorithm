# 숫자 세개를 담을 리스트 numbers
numbers = list(map(int, input().split()))

for i in range(3):
    for j in range(i, 3):
        if numbers[i] >= numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(*numbers)

import heapq

# 숫자 세개를 담을 리스트 numbers
numbers = list(map(int, input().split()))
heapq.heapify(numbers)
while numbers:
    print(heapq.heappop(numbers), end=' ')