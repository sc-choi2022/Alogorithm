import sys

def turn(number):
    tmp = graph[0+number][number+number]

    for j in range(0+number, M-number):
        graph[0+number][j] = graph[0+number][j+1]

    for i in range(N-number+1, 0+number, -1):

# 배열의 크기 N, M 회전시킨 결과 R
N, M, R = map(int, sys.stdin.readline().split())
# 배열 graph
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for n in range(min(N, M)//2):
    turn(n)