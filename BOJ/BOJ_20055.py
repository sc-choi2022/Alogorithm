from collections import deque
import sys
# 컨베이어 벨트의 길이 N, 내구도 0인 칸의 개수 조건 K
N, K = map(int, sys.stdin.readline().split())
# 컨베이어의 내구도를 저장하는 배열 conveyor
conveyor = deque(list(map(int, sys.stdin.readline().split())))
robots = [0]*(2*N)

