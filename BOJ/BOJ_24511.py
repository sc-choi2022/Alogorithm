from collections import deque
import sys

# 자료구조의 개수 N
N = int(sys.stdin.readline())

# 자료구조를 저장하는 배열 A
A = list(map(int, sys.stdin.readline().split()))
# 수열 B
B = deque(list(map(int, sys.stdin.readline().split())))
# 삽입할 수열의 길이 M
M = int(sys.stdin.readline())
# queuestack에 삽입할 원소를 담고 있는 수열 C
C = list(map(int, sys.stdin.readline().split()))