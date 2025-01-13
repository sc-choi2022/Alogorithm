from copy import deepcopy
import sys

# R1: 배열을 상하 반전
def R1():
    for i in range(N):
        graph[i] = pre[-i-1]

# R2: 배열을 좌우 반전
def R2():
    for i in range(N):
        graph[i] = pre[i][::-1]

# 오른쪽으로 90도 회전
def R3():
    global graph, N, M
    graph = list(map(list, zip(*graph[::-1])))
    N, M = M, N

# 왼쪽으로 90도 회전
def R4():
    global graph, N, M
    graph = list(map(list, zip(*graph)))[::-1]
    N, M = M, N

# 1번 그룹의 부분 배열을 2번 그룹 위치로, 2번을 3번으로, 3번을 4번으로, 4번을 1번으로 이동
def R5():
    return

# 1번 그룹의 부분 배열을 4번 그룹 위치로, 4번을 3번으로, 3번을 2번으로, 2번을 1번으로 이동
def R6():
    return

# 배열의 크기 N, M, 연산의 수 R
N, M, R = map(int, sys.stdin.readline().split())
# 배열을 저장하는 graph
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 수행해야하는 연산을 저장하는 배열 orders
orders = list(map(int, sys.stdin.readline().split()))

for order in orders:
    # 바로 전 배열을 저장하는 배열 pre
    pre = deepcopy(graph)
    if order == 1:
        R1()
    elif order == 2:
        R2()
    elif order == 3:
        R3()
    elif order == 4:
        R4()
    elif order == 5:
        R5()
    else:
        R6()

for g in graph:
    print(*g)