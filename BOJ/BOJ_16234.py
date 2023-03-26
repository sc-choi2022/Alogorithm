from collections import deque
import sys

# N×N 크기의 땅, L명 이상, R명 이하
N, L, R = map(int, sys.stdin.readline().split())
# 각 나라의 인구수를 담을 배열 nation
nation = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 인구 이동이 일어나는 일수 day
day = 0