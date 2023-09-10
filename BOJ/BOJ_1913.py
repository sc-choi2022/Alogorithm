import sys
# NxN의 표의 길이인 홀수 N
N = int(sys.stdin.readline())
# 위치를 찾고자 하는 N^2이하의 자연수 하나 M
M = int(sys.stdin.readline())

numbers = [[0]*N for _ in range(N)]
cnt = 1
# M의 위치 mi, mj
mi, mj = 0, 0