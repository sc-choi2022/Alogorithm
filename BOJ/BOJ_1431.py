from collections import deque
import sys

# 시리얼번호의 개수 N
N = int(sys.stdin.readline())
numbers = {}

for _ in range(N):
    number = sys.stdin.readline().strip()
    add = 0
    for n in number:
        if n.isdigit():
            add += int(n)
    numbers[number] = add

ans = sorted(numbers.items(), key=lambda x: (len(x), x[1], x))

for a in ans:
    print(a[0])