from collections import deque
import sys

# 자리수의 합을 구하는 함수 checkNum
def checkNum(xx):
    add = 0
    for x in xx:
        if x.isdigit():
            add += int(x)
    return add

# 시리얼번호의 개수 N
N = int(sys.stdin.readline())
# 시리얼번호를 담는 배열 numbers
numbers = [sys.stdin.readline().strip() for _ in range(N)]
# 주어지는 3개의 조건 순서로 정렬
numbers.sort(key=lambda x: (len(x), checkNum(x), x))

# numbers를 출력
for number in numbers:
    print(number)