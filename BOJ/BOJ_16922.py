from itertools import combinations_with_replacement
import sys

N = int(sys.stdin.readline())
result = set()
roman = [1, 5, 10, 50]

for numbers in combinations_with_replacement([0, 1, 2, 3], N):
    tmp = 0
    for number in numbers:
        tmp += roman[number]
    result.add(tmp)

print(len(result))