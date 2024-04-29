import sys

# 굴다리의 길이 N
N = int(sys.stdin.readline())
# 가로등을 설치할 개수
M = int(sys.stdin.readline())
# 가로등의 위치를 저장하는 배열 position
position = list(map(int, sys.stdin.readline().split()))
# 가로등의 최소 높이 height
height = max(N-position[M-1], position[0])

for i in range(1, M-1):
    height = max(height, (position[i]-position[i-1]+1)//2)

# 굴다리의 길이 N을 모두 비추기 위한 가로등의 최소 높이를 출력
print(height)