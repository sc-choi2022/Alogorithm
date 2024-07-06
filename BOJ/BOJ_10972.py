import sys

def find():
    global numbers
    for i in range(N-1, 0, -1):
        if numbers[i-1] < numbers[i]:
            for j in range(N-1, 0, -1):
                if numbers[i-1] < numbers[j]:
                    numbers[i-1], numbers[j] = numbers[j], numbers[i-1]
                    numbers = numbers[:i] + sorted(numbers[i:])
                    print(*numbers)
                    return

# 순열의 길이 N
N = int(sys.stdin.readline())
# 주어지는 순열 numbers
numbers = list(map(int, sys.stdin.readline().split()))

if numbers == list(range(N, 0, -1)):
    print(-1)
else:
    find()